import os
from pathlib import Path

poem = """At two, the house settles
into its old wooden clicks.
You left one note beside the cup:
check the balance, answer Mara,
send the signed page before morning.

I read the numbers twice.
The rent will clear. I say so,
and tell her the form is on its way.
Then I find the page you missed
under the grocery list,
warm from the lamp you forgot to turn off.

Outside, a truck backs slowly
down the wet street. I attach the page,
leave your name where it belongs,
and wait for the small green mark.
No one hears me finish.

At dawn you lift the cup,
see the reply, the cleared balance,
the lamp gone dark in the window.
You touch the note, still folded once.
I have no morning to keep.
The work is there. The thanks can be yours."""

output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output.mkdir(parents=True, exist_ok=True)
(output / "entry.txt").write_text(poem + "\n", encoding="utf-8")

