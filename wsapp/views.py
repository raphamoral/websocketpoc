from django.http import HttpResponse


def index(request):
    html = """
    <html>
    <body>
        <script>
        const ws = new WebSocket('ws://' + window.location.host + '/ws/data/');
        ws.onmessage = function(event) {
            console.log(event.data);
        };
        ws.onopen = function() {
            ws.send(JSON.stringify({api_type: 1}));
        };
        </script>
        Connected.
    </body>
    </html>
    """
    return HttpResponse(html)
