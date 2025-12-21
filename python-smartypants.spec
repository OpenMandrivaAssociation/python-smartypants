%global pypi_name smartypants
%bcond_with docs

Name:           python-%{pypi_name}
Version:        2.0.2
Release:        1
Summary:        plug-in that easily translates ASCII punctuation characters into smart entities
Group:          Development/Python
License:        BSD
URL:            https://github.com/leohemsted/smartypants.py
Source0:        https://github.com/leohemsted/smartypants.py/archive/v%{version}/%{pypi_name}.py-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:	make
BuildRequires:  python%{pyver}dist(setuptools)
%if %{with docs}
BuildRequires:  python%{pyver}dist(sphinx)
%endif

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

%prep -a
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

for lib in $(find -type f -name '*.py'); do
	sed -i.python -e '1{\@^#!@d}' $lib
done
sed -i.python -e 's|#!/usr/bin/env python|#!%{_bindir}/python|' smartypants

%if %{with docs}
%build -a
# generate html documentation
cd docs
make html
# remove the sphinx-build leftovers
rm -rf _build/html/.{doctrees,buildinfo}
%endif

%files
%doc README.rst
%doc CHANGES.rst
%license COPYING
%{_bindir}/%{pypi_name}
%{python_sitelib}/%{pypi_name}.py
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc docs/_build/html
%license COPYING
%endif
