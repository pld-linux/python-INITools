Summary:	Tools for parsing and using INI-style files
Summary(pl.UTF-8):	Narzędzia do przetwarzania i używania plików w stylu INI
Name:		python-INITools
Version:	0.3.1
Release:	1
License:	X11/MIT
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/I/INITools/INITools-%{version}.tar.gz
# Source0-md5:	1e46bf333e93abeb5b5a827169a80dca
URL:		http://pythonpaste.org/initools/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of tools for parsing and using .ini-style files, including an
abstract parser and several tools built on that parser.

%description -l pl.UTF-8
Zestaw narzędzi do przetwarzania plików w stylu .ini, w tym
abstrakcyjny parser i kilka narzędzi stworzonych w oparciu o ten
parser.

%prep
%setup -q -n INITools-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/initools*
%{py_sitescriptdir}/INITools*
