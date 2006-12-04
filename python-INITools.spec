Summary:	Tools for parsing and using INI-style files
Summary(pl):	Narzêdzia do przetwarzania i u¿ywania plików w stylu INI
Name:		python-INITools
Version:	0.2
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/I/INITools/INITools-%{version}.tar.gz
# Source0-md5:	23bf98b52aa9d8fe38d2467fcecf1071
URL:		http://pythonpaste.org/initools/
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of tools for parsing and using .ini-style files, including an
abstract parser and several tools built on that parser.

%description -l pl
Zestaw narzêdzi do przetwarzania plików w stylu .ini, w tym
abstrakcyjny parser i kilka narzêdzi stworzonych w oparciu o ten
parser.

%prep
%setup -q -n INITools-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%{py_sitescriptdir}/initools*
%{py_sitescriptdir}/INITools*
