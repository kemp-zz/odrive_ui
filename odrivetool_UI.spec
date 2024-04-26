# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


additional_imports = [
    'fibre',  
    'PyQt5',  
    'pyqtgraph',  
    'odrive'  
]

a = Analysis(['odrivetool_UI.py'],
             pathex=['<where-your-python-path>'],  
             binaries=[],
             datas=[],
             hiddenimports=additional_imports, 
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='odrivetool_UI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False ) 
