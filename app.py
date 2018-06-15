from flask import Flask, render_template, current_app, Markup
import json
from jinja2 import Template
app = Flask(__name__)
app.debug = True
app.secret_key = 'development key'



from pyhocon import ConfigFactory


def load_html(conf_prim):
    html = """

        """

    for item in conf_prim:
        html += """<div class="page-header"><h1>{}""".format(item["name"])
        if item['turtles'] == True:
            html += """&nbsp;<img src="/static/icons/turtle.gif">"""
        if item['patches'] == True:
            html += """&nbsp;<img src="/static/icons/patch.gif">"""
        html += "</h1></div>"
        if item['tag'] == "Any":
            html +="""<p style="font-size:1.2em"><b>any? <i>agentset</i> </b></p>"""
        if item['tag'] == "Count":
            html +="""<p style="font-size:1.2em"><b>count <i>agentset</i> </b></p>"""
        html += """<p>{}</p>""".format(item['description'])
        if item['textbox'] == True:
            html += """<pre style="border: none; margin-bottom: 0">
            {}
            </pre>""".format(item['text'])
        html += """<p>&nbsp;</p>"""
        html += """<p><a class="btn btn-primary" role="button" data-toggle="collapse" href="#collapse{}" aria-expanded="false" aria-controls="collapseExample">
                Try it yourself &nbsp;&nbsp;&nbsp;<span class="glyphicon glyphicon-menu-down" aria-hidden="true"></span>
                </a></p>
                <div class="collapse" id="collapse{}">
                  <div class="row">
                    <div class="col-md-5">
                      <div class="well" style="padding: 10px;">


              <textarea id="usercode{}"
                class="form-control small"
                rows="20"
                style="font-family: Menlo, Monaco, Consolas, monospace; width: 100%; margin-bottom: 20px;"
                >
                {}
                </textarea>
                            <p class="text-center">
                              <button id="compile{}" type="button" class="btn btn-success" href="#" ><span class="glyphicon glyphicon-play" aria-hidden="true"></span> Compile</button>
                              &nbsp;
                              <button id="reset{}" type="button" class="btn btn-default" href="#"><span class="glyphicon glyphicon-play" aria-hidden="true"></span> Reset</button>
                            </p>
                          </div>
                        </div>
                        <div class="col-md-7">
                          <iframe id="codeframe{}" src="/static/codetemplate.html" class="col-md-12" scrolling="no" style="height: 500px; border: none; "></iframe>
                        </div>
                      </div>
                    </div>
                <script>
                    (function() {{

                        var id = "{}";
                        var editor = CodeMirror.fromTextArea(document.getElementById("usercode"+id), {{
                            mode: "netlogo",
                            theme: "netlogo-default"
                        }});
                        document.getElementById("compile"+id).addEventListener("click",function(){{compilecode(id,editor.getValue())}});
                    }})()
                </script>

                """.format(item["tag"],item["tag"],
                           item["tag"],item["trywidget"]["code"],
                           item["tag"],item["tag"],
                           item["tag"],item["tag"],
                           item["tag"])

        html += """<p><small style="float: right; vertical-align: middle"><strong>keywords:</strong> {}</small></p>""".format(item['keywords'])
    return html


@app.route('/debug')
def index():
    logging.warning("See this message in Flask Debug Toolbar!")
    return "<html><body></body></html>"

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/agentset")
def agentset():

    agentset_conf = ConfigFactory.parse_file('conf/agentset.conf')
    agentset_prim = agentset_conf.get_list('primitives')

    html = load_html(agentset_prim);

    return render_template('agentset.html',task=Markup(html))

@app.route("/interface")
def interface():
    return render_template('interface.html')

@app.route("/interfaceTab")
def interfaceTab():
    return render_template('interfaceTab.html')

@app.route("/infoTab")
def infoTab():
    return render_template('infoTab.html')

@app.route("/codeTab")
def codeTab():
    return render_template('codeTab.html')

@app.route("/commandcenter")
def commandcenter():
    return render_template('commandcenter.html')

@app.route("/agents")
def agents():
    return render_template('agents.html')

@app.route("/turtles")
def turtles():
    return render_template('turtles.html')

@app.route("/basiclinks")
def basiclinks():
    return render_template('basiclinks.html')

@app.route("/shapes")
def shapes():
    return render_template('shapes.html')

@app.route("/toolshubnet")
def toolshubnet():
    return render_template('toolshubnet.html')

@app.route("/behaviorspace")
def behaviorspace():
    return render_template('behaviorspace.html')

@app.route("/behaviorsearch")
def behaviorsearch():
    return render_template('behaviorsearch.html')

@app.route("/monitors")
def monitors():
    return render_template('monitors.html')

@app.route("/systemmodeler")
def systemmodeler():
    return render_template('systemmodeler.html')

@app.route("/color")
def color():
    color_conf = ConfigFactory.parse_file('conf/color.conf')
    color_prim = color_conf.get_list('primitives')

    html = load_html(color_prim);

    return render_template('color.html',task=Markup(html))

@app.route("/colors")
def colors():
    return render_template('colors.html')

@app.route("/math")
def math():
    conf = ConfigFactory.parse_file('conf/math.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('math.html',task=Markup(html))

@app.route("/patch")
def patch():
    conf = ConfigFactory.parse_file('conf/patch.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('patch.html',task=Markup(html))

@app.route("/patches")
def patches():
    return render_template('patches.html')

@app.route("/procedures")
def procedures():
    return render_template('procedures.html')

@app.route("/variables")
def variables():
    conf = ConfigFactory.parse_file('conf/variables.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('variables.html',task=Markup(html))

@app.route("/anonymous")
def anonymous():
    conf = ConfigFactory.parse_file('conf/anonymous.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('anonymous.html',task=Markup(html))

@app.route("/control")
def control():
    conf = ConfigFactory.parse_file('conf/control.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('control.html',task=Markup(html))

@app.route("/file")
def file():
    conf = ConfigFactory.parse_file('conf/file.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('file.html',task=Markup(html))

@app.route("/inputoutput")
def inputoutput():
    conf = ConfigFactory.parse_file('conf/inputoutput.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('inputoutput.html',task=Markup(html))

@app.route("/hubnet")
def hubnet():
    conf = ConfigFactory.parse_file('conf/hubnet.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('hubnet.html',task=Markup(html))

@app.route("/links")
def links():
    conf = ConfigFactory.parse_file('conf/links.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('links.html',task=Markup(html))

@app.route("/list")
def list():
    conf = ConfigFactory.parse_file('conf/list.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('list.html',task=Markup(html))

@app.route("/perspective")
def perspective():
    conf = ConfigFactory.parse_file('conf/perspective.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('perspective.html',task=Markup(html))

@app.route("/plotting")
def plotting():
    conf = ConfigFactory.parse_file('conf/plotting.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('plotting.html',task=Markup(html))

@app.route("/system")
def system():
    conf = ConfigFactory.parse_file('conf/system.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('system.html',task=Markup(html))

@app.route("/string")
def string():
    conf = ConfigFactory.parse_file('conf/string.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('string.html',task=Markup(html))

@app.route("/turtle")
def turtle():
    conf = ConfigFactory.parse_file('conf/turtle.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('turtle.html',task=Markup(html))

@app.route("/keywords")
def keywords():
    conf = ConfigFactory.parse_file('conf/keywords.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('keywords.html',task=Markup(html))

@app.route("/constants")
def constants():
    conf = ConfigFactory.parse_file('conf/constants.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('constants.html',task=Markup(html))

@app.route("/world")
def world():
    conf = ConfigFactory.parse_file('conf/world.conf')
    prim = conf.get_list('primitives')

    html = load_html(prim);

    return render_template('world.html',task=Markup(html))

@app.route("/introtutorials")
def introtutorials():
    return render_template('introtutorials.html')

@app.route("/codeexamples")
def codeexamples():
    return render_template('codeexamples.html')

@app.route("/videos")
def videos():
    return render_template('videos.html')


#NOT TYPICAL WEBPAGE
@app.route("/hatch")
def hatch():
    return current_app.send_static_file('hatch.html')


@app.route("/codetemplate")
def codetemplate():
    return current_app.send_static_file('codetemplate.html')




if __name__ == "__main__":
    app.run()
