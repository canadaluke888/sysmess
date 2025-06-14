from setuptools import setup, Extension

module = Extension(
    name="sysmess",
    sources=["src/sysmessmodule.c"],
)

setup(
    name="sysmess",
    version="0.1",
    description="Fancy terminal message box renderer",
    ext_modules=[module],
)