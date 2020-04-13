import os

from setuptools import find_namespace_packages, setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.md"), encoding="utf-8") as fd:
    long_description = fd.read()

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        """
        Patch bdist_wheel to force package as platform wheel.
        
        Reference:
            https://stackoverflow.com/a/45150383
        """

        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False


except ImportError:
    bdist_wheel = None

setup(
    # published project name
    name="utoolbox-template",
    # from dev to release
    #   bumpversion release
    # to next version
    #   bump patch/minor/major
    version="0.0.1.dev0",
    # one-line description for the summary field
    description="Template package for uToolbox namespace package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # project homepage
    url="https://github.com/liuyenting/utoolbox-template",
    # name or organization
    author="Liu, Yen-Ting",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
    ],
    keywords="microscopy",
    packages=find_namespace_packages(include=["utoolbox.*"]),
    python_requires="~=3.7",
    # use pyproject.toml to define build system requirement
    # setup_requires=[
    # ],
    # other packages the project depends on to run
    #   install_requires -> necessity
    #   requirements.txt
    install_requires=["utoolbox-core"],
    # additional groups of dependencies here for the "extras" syntax
    extras_require={},
    # data files included in packages
    # package_data={"": ["*.cu"]},
    # include all package data found implicitly
    # include_package_data=True,
    # data files outside of packages, installed into '<sys.prefix>/my_data'
    data_files=[],
    # executable scripts
    entry_points={"console_scripts": []},
    # command hooks
    cmdclass={"bdist_wheel": bdist_wheel},
    # project is compressable
    zip_safe=True,
)
