# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['shmup.py'],
    pathex=['/Users/ulia/PycharmProjects/pygame_inspo'],
    binaries=[],
    datas=[('./img', 'img'), ('./snd', 'snd')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='shmup',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
app = BUNDLE(
    exe,
    name='shmup.app',
    icon='/Users/ulia/PycharmProjects/pygame_inspo/img/ship.ico',
    bundle_identifier=None,
)
