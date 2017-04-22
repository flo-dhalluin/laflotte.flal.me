# custom plugin for cuvee generation
# quite inspired from the blog plugin example

CUVEES = []

def preBuild(site) :

    global CUVEES
    cuvees_list = []

    for page in site.pages():
        if page.path.startswith("cuvees/") :

            page_context = page.context()

            if "id" in page_context :
                cuvee_id = page_context["id"]
            else :
                # getting it from the filename
                fname = page.path.split("/")[-1]
                raw_id = fname.split("-")[0]
                raw_id = raw_id.split("_")[0]

                cuvee_id = raw_id

            cuvee = {
                "id": cuvee_id,
                "name": page_context.get("name", "Anonymous"),
                "path": page.path,
            }
            cuvees_list.append(cuvee)

    CUVEES = sorted(cuvees_list, key=lambda x:x["id"])


def preBuildPage(site, page, context, data):
    # inject the table in context
    context['cuvees'] = CUVEES
    return context, data
