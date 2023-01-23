<h1 align="center">Find Best Box</h1>
<h2 align="center">📦</h2>



Script para encontrar as melhores caixas focando diminuir o desperdício de espaço vazio e a quantidade de caixas a serem feitas

<br>
<br>

<h3>Exemplo</h3>

```
boxes = [10, 5, 20, 25, 30, 40, 60, 70, 90, 100, 386]

total_volume = 186
print(cube_volumes(total_volume, boxes), 186)
retorno [90, 100]

total_volume = 121
print(cube_volumes(total_volume, boxes), 121)
retorno [25, 100]

total_volume = 116
print(cube_volumes(total_volume, boxes), 116)
retorno [20, 100]

total_volume = 110
print(cube_volumes(total_volume, boxes), 110)
retorno [10, 100]

total_volume = 106
print(cube_volumes(total_volume, boxes), 106)
retorno [10, 100]

total_volume = 386
print(cube_volumes(total_volume, boxes), 386)
retorno [386]

total_volume = 86
print(cube_volumes(total_volume, boxes), 86)
retorno [90]

total_volume = 56
print(cube_volumes(total_volume, boxes), 56)
retorno [60]

total_volume = 12
print(cube_volumes(total_volume, boxes), 12)
retorno [20]

total_volume = 1.2
print(cube_volumes(total_volume, boxes), 1.2)
retorno [5]

total_volume = 8
print(cube_volumes(total_volume, boxes), 8)
retorno [10]

total_volume = 520
print(cube_volumes(total_volume, boxes), 520)
retorno [386, 5, 30, 100]

total_volume = 564
print(cube_volumes(total_volume, boxes), 564)
retorno [386, 10, 70, 100]

total_volume = 38
print(cube_volumes(total_volume, boxes), 38)
retorno [40]

```


</code>
