from flask import Flask,Response,request,render_template,redirect,jsonify  
import pyodbc

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show():

    html = """<html>
                <head>
                    <title>Analyze Sample</title>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                </head>
                <body>
                
                <script type="text/javascript">
                    function processImage() {
                        // **********************************************
                        // *** Update or verify the following values. ***
                        // **********************************************
                
                        // Replace <Subscription Key> with your valid subscription key.
                        var subscriptionKey = "777441aab2e544bf94f6eb80adf9f4a7";
                
                        // You must use the same Azure region in your REST API method as you used to
                        // get your subscription keys. For example, if you got your subscription keys
                        // from the West US region, replace "westcentralus" in the URL
                        // below with "westus".
                        //
                        // Free trial subscription keys are generated in the "westus" region.
                        // If you use a free trial subscription key, you shouldn't need to change
                        // this region.
                        var uriBase =
                            "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/analyze";
                
                        // Request parameters.
                        var params = {
                            "visualFeatures": "Categories,Description,Color",
                            "details": "",
                            "language": "en",
                        };
                
                        // Display the image.
                        var sourceImageUrl = document.getElementById("inputImage").value;
                        document.querySelector("#sourceImage").src = sourceImageUrl;
                
                        // Make the REST API call.
                        $.ajax({
                            url: uriBase + "?" + $.param(params),
                
                            // Request headers.
                            beforeSend: function(xhrObj){
                                xhrObj.setRequestHeader("Content-Type","application/json");
                                xhrObj.setRequestHeader(
                                    "Ocp-Apim-Subscription-Key", subscriptionKey);
                            },
                
                            type: "POST",
                
                            // Request body.
                            data: '{"url": ' + '"' + sourceImageUrl + '"}',
                        })
                
                        .done(function(data) {
                            // Show formatted JSON on webpage.
                            $("#responseTextArea").val(JSON.stringify(data, null, 2));
                        })
                
                        .fail(function(jqXHR, textStatus, errorThrown) {
                            // Display error message.
                            var errorString = (errorThrown === "") ? "Error. " :
                                errorThrown + " (" + jqXHR.status + "): ";
                            errorString += (jqXHR.responseText === "") ? "" :
                                jQuery.parseJSON(jqXHR.responseText).message;
                            alert(errorString);
                        });
                    };
                </script>
                
                <h1>Analyze image:</h1>
                Enter the URL to an image, then click the <strong>Analyze image</strong> button.
                <br><br>
                Image to analyze:
                <input type="text" name="inputImage" id="inputImage"
                    value="https://upload.wikimedia.org/wikipedia/commons/3/3c/Shaki_waterfall.jpg" />
                <button onclick="processImage()">Analyze image</button>
                <br><br>
                <div id="wrapper" style="width:1020px; display:table;">
                    <div id="jsonOutput" style="width:600px; display:table-cell;">
                        Response:
                        <br><br>
                        <textarea id="responseTextArea" class="UIInput"
                                style="width:580px; height:400px;"></textarea>
                    </div>
                    <div id="imageDiv" style="width:420px; display:table-cell;">
                        Source image:
                        <br><br>
                        <img id="sourceImage" width="400" />
                    </div>
                </div>
                </body>
                </html>""" 

    

    return Response(response = html, status = 200, mimetype = "text/html")

# @app.route('/doform', methods=['POST'])
# def savedata():
#     _name = request.form['name']
#     _email = request.form['email']
#     _designation = request.form['designation']
#     _company = request.form['company']

#     sql = "INSERT INTO register(Name, Email, Designation, Company) VALUES('{}', '{}', '{}', '{}')".format(_name, _email, _designation, _company)
#     connection = pyodbc.connect('Driver={SQL Server};Server=dcdappserver.database.windows.net;Database=dicodingdb;uid=dicoding;pwd=Arya1234')
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     connection.commit()
#     connection.close()

#     return redirect("https://dcdsubmission1.azurewebsites.net/", code=302)


