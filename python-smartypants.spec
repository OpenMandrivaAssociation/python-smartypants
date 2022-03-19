%global pypi_name smartypants

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        2
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities
Group:          Development/Python
License:        BSD
URL:            https://github.com/leohemsted/smartypants.py
Source0:        https://github.com/leohemsted/smartypants.py/archive/v%{version}/%{pypi_name}.py-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.

%package -n python-%{pypi_name}-doc
Summary:        python-smartypants documentation
Group:          Documentation

%description -n python-%{pypi_name}-doc
Documentation for python-smartypants.

%prep
%autosetup -n %{pypi_name}.py-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find -type f -name '*.py'); do
 sed -i.python -e '1{\@^#!@d}' $lib
done
sed -i.python -e 's|#!/usr/bin/env python|#!/usr/bin/python3|' smartypants

%build
%py3_build

# generate html documentation
cd docs
make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}

%install
%py_install

%files
%doc README.rst
%doc CHANGES.rst
%license COPYING
%{_bindir}/%{pypi_name}
%{python_sitelib}/__pycache__/*
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc docs/_build/html
%license COPYING
