from rich.console import Console
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree("[link=https://www.linkedin.com/in/yvann-le-fay/]Yvann Le Fay", guide_style="bold bright_black")

self_tree = tree.add("code for me", guide_style="bright_black")
self_tree.add("[bold link=https://github.com/hallelujahylefay/independent_component_analysis]independent_component_analysis[/] - [bright_black]FastICA and variational autoencoders, jax backend")
self_tree.add("[bold link=https://github.com/hallelujahylefay/bayesianSDEsolver]bayesianSDEsolver[/] - [bright_black]efficient SDE samplers, jax backend")
self_tree.add("[bold link=https://github.com/hallelujahylefay/abelian_sandpile_ensae]abelian_sandpile_ensae[/] - [bright_black]dynamical system exhibiting self-organised criticality")


contrib_tree = tree.add("code I helped with", guide_style="bright_black")
contrib_tree.add("[bold link=https://github.com/hallelujahylefay/NeuroLang]NeuroLang[/] - [bright_black]probabilistic logic programming")

future_tree = tree.add("code I want to share", guide_style="bright_black")
future_tree.add("[bold link=https://github.com/nchopin/particles]particles[/] - [bright_black]SMC in python")
future_tree.add("[bold link=https://github.com/blackjax-devs/blackjax]blackjax[/] - [bright_black]samplers in jax")
future_tree.add("[bold link=https://github.com/probml/dynamax]dynamax[/] - [bright_black]state space models in jax")

work_tree = tree.add("work", guide_style="bright_black")
ens_tree = work_tree.add("École Normale Supérieure Paris-Saclay")
ens_tree.add("M.Sc., Machine Learning (MVA)")
ensae_tree = work_tree.add("ENSAE")
ensae_tree.add("M.Eng., Financial Engineering and Statistics")
aalto = work_tree.add("Aalto University - [bright_black]Research Assistant")
inria = work_tree.add("INRIA - [bright_black]Research Assistant")
lombard = work_tree.add("Lombard Odier Investment Managers - [bright_black]Quantitative Researcher")

console.print(tree)
console.print("")
console.print("[green]Feel free to reach me: {firstname}[dot]{lastname}[at]ensae[dot]fr, +33 6 45 44 70 93. My [bold link=https://github.com/hallelujahylefay/curriculum-vitae/blob/main/CV.pdf]curriculum vitæ[/].")

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)