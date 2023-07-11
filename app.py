from flask import Flask,render_template,url_for,request

SOURCES=['gov.uk','BBC','SkyNews'] #possible sources, authors, types etc...
AUTHORS=['Reportes','Government']
TYPES=['Reports','Articles','Audits']
app=Flask(__name__)
app.static_folder='./static'

@app.route('/',methods=['POST','GET'])
def index():
          if request.method == 'POST': #query posted to this method
                  print("QUERY IS: " + request.form['query']) 
          return render_template('main.html', sources=SOURCES, authors=AUTHORS,types=TYPES
          )



'''''''''
@app.route("/search_genappbuilder", methods=["POST"])
def search_genappbuilder(search_query) -> str:
    """
    Handle Search Gen App Builder Request
    """

    # Check if POST Request includes search query
    if not search_query:
        return render_template('main.html', sources=SOURCES, authors=AUTHORS,types=TYPES
          )

    results, request_url, raw_request, raw_response = search_enterprise_search(
        project_id=PROJECT_ID,
        location=LOCATION,
        search_engine_id=CUSTOM_UI_DATASTORE_IDS[0]["datastore_id"],
        search_query=search_query,
    )

    return render_template(
        "search.html",
        nav_links=NAV_LINKS,
        message_success=search_query,
        results=results,
        request_url=request_url,
        raw_request=raw_request,
        raw_response=raw_response,
    )
'''''''''

if __name__=="__main__":
        app.run(debug=True)

