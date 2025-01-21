from ase.spacegroup import crystal
from ase.io import write

# 格子定数（例: Teの値）
a = 4.454  # 格子定数a [Å]
c = 5.924  # 格子定数c [Å]

# 左手系のP3221構造を生成 (3a Wyckoff位置に対応する座標を全て指定)
te = crystal(
    symbols='Te',
    basis=[(0.269, 0.0, 1/3), (-0.269, -0.269, 2/3), (0.0, 0.269, 0.0)],  
    spacegroup = 154,  # P3221の空間群番号
    cellpar=[a, a, c, 90, 90, 120]
)

# cifファイルに書き出し
write('left_handed_te_P3221_fixed.cif', te)
print("Left-handed P3221 Te structure written to 'left_handed_te_P3221_fixed.cif'")