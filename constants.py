def true(x):
    return f"""<meta id="fuck" content="fuck {x}" property="og:title" />
<!DOCTYPE html>
<html lang="en">
<head>
<meta content="i hate {x}" property="og:description" />
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>fuck {x}</title>
<script type='text/javascript'>\
  title = "fuck {x} ";
  position = 0;
  function scrolltitle() {{
    document.title = title.substring(position, title.length) + title.substring(0, position);
    position++;
    if (position > title.length) position = 0;
    titleScroll = window.setTimeout(scrolltitle,200);
  }}
  scrolltitle();
</script>
</head>
<style>
  *{{
    overflow: hidden;
  }}
  #troll {{
    font-size: 70px;
    width: fit-content;
    color: white;
  }}
  body {{
    background-color: black;
  }}
</style>
<body>
  <div id="troll">fuck {x}</div>
</body>
<script>
const section = document.body;
const text = troll;
const FPS = 60;
const colors = ['red','pink']
section.style.height = window.innerHeight + "px";
section.style.width = window.innerWidth + "px";

let xPosition = 10;
let yPosition = 10;
let xSpeed = 4;
let ySpeed = 4;
text.style.transition = "color 1000ms linear";
function update() {{
  text.style.transform = `translateX(${{xPosition}}px) translateY(${{yPosition}}px)`
}}

setInterval(() => {{
  if (xPosition + text.clientWidth >= window.innerWidth || xPosition <= 0) {{
    xSpeed = -xSpeed;
  }}
  if (yPosition + text.clientHeight >= window.innerHeight || yPosition <= 0) {{
    ySpeed = -ySpeed;
  }}
  text.style.color = colors[parseInt(Math.random() * ((colors.length - 1) - 1) + 1)];
  xPosition += xSpeed;
  yPosition += ySpeed;
  update();
}}, 1000 / FPS);

window.addEventListener("resize", () => {{
  xPosition = 10;
  yPosition = 10;

  section.style.height = window.innerHeight + "px";
  section.style.width = window.innerWidth + "px";
}});

</script>
</html>"""

false = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta id="fuck" content="!!!!!!!bullshittery" property="og:title" />
    <meta content="good try" property="og:description" />
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>fuck you</title>
  </head>
  <body>
    gosh i love cbt
  </body>
</html>"""