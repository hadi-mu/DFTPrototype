from flask import Flask,render_template,url_for,request

SOURCES=['gov.uk','BBC','SkyNews'] #possible sources, authors, types etc...
AUTHORS=['Reporters','Government']
TYPES=['Reports','Articles','Audits']
dateRange=""
sourcesToUse=[]
authorsToUse=[]
typesToUse=[]
sumText="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
prevHeadings=["Provisional Report 2022","Car Accidents 2019","Fishing Accidents 2021"]
prevText=[" Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of  (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum comes from a line in section 1.10.32."]*3
app=Flask(__name__)
app.static_folder='./static'


@app.route('/',methods=['POST','GET'])
def index():
          if request.method == 'POST': #query posted to this method
                  print("QUERY IS: " + request.form['query']) 
          return render_template('main.html', sources=SOURCES, authors=AUTHORS,types=TYPES,summary=sumText,headings=prevHeadings,previewText=prevText
          )

@app.route('/date',methods=['POST','GET'])

def changeDate():
         if request.method == 'POST': #query posted to this method
                  dateRange=request.form['start']+':'+request.form['end']
                  print("Dates selected are " + dateRange)
         return render_template('main.html', sources=SOURCES, authors=AUTHORS,types=TYPES,summary=sumText,headings=prevHeadings,previewText=prevText
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

