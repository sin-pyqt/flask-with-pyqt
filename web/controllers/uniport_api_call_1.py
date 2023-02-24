import requests
import json


def fetch_uniport_details(uniport_id):
    final_url = (
        "https://www.ebi.ac.uk/chembl/api/data/target/search?limit=1000&offset=0&format=json&q="
        + uniport_id
    )

    response = requests.get(final_url)

    d = json.loads(response.text)
    resp = d["targets"]
    return resp[0]


def get_uniport_primary_details(uniport_id):
    # response = fetch_uniport_details("P1234")
    response = fetch_uniport_details(uniport_id)
    d = dict()
    for x in response.keys():
        if (
            x == "target_components"
            or x == "target_components_synonyms"
            or x == "cross_references"
        ):
            continue
        d[x] = response[x]
    return d


def get_uniport_target_component_synonyms(uniport_id):
    # response = fetch_uniport_details("P1234")
    response = fetch_uniport_details(uniport_id)
    temp = response["target_components"]
    return temp[0]["target_component_synonyms"]


# ans = fetch_uniport_details("P1234")
# # print(ans)
# # ans = get_unpiport_primary_details(ans)
# ans = get_unpiport_target_component_synonyms(ans)
# print(ans)
