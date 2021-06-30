%global pypi_name smartypants

Name:           python-%{pypi_name}
Version:        2.0.1
Release:        
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities
Group:          Development/Python
License:        BSD
URL:            https://github.com/leohemsted/smartypants.py
Source0:        %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
SmartyPants is a free web publishing plug-in for Movable
Type, Blosxom, and BBEdit that easily translates plain ASCII
punctuation characters into “smart” typographic punctuation HTML
entities.

%package -n     python3-%{pypi_name}
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities
Group:          Development/Python
Requires:       python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
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
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%doc CHANGES.rst
%license COPYING
%{_bindir}/%{pypi_name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc docs/_build/html
%license COPYING
