Summary:	The f2c Fortran to C/C++ conversion program
Summary(pl.UTF-8):	Program f2c do tłumaczenia z Fortranu na C/C++
Name:		f2c
Version:	20031027
Release:	3
License:	Distributable
Group:		Development/Languages/Fortran
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	bcd2c9ba1307c9fc9f73027c3c4e3d4c
Patch0:		%{name}-20031027.patch
URL:		ftp://ftp.netlib.org/f2c/
BuildRequires:	rpmbuild(macros) >= 1.583
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
f2c converts Fortran 77 source code to C or C++ source files. If no
Fortran files are named on the command line, f2c can read Fortran from
standard input and write C to standard output.

f2c can also be used (with the -P option) to generate ANSI C header
files for calling Fortran routines from C.

%description -l pl.UTF-8
f2c służy do tłumaczenia kodu źródłowego w Fortranie 77 na kod
dając w wyniku pliki z kodem źródłowym w C lub C++. Jeśli w wierszu
polecenia nie zostaną podane żadne pliki, f2c będzie oczekiwał kodu w
Fortranie na standardowym wejściu i pisał kod w C na standardowe
wyjście.

f2c może również służyć (z opcją -P) do generowania plików
nagłówkowych ANSI C w celu wywoływania procedur fortranowskich z C.

%prep
%setup -q
%patch -P0 -p1

%build
%ifarch alpha
MFLAG=-mieee
%endif

cp -f src/makefile.u src/Makefile
%{__make} -C src f2c \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	MFLAG="$MFLAG"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir},%{_includedir}}

install src/f2c $RPM_BUILD_ROOT%{_bindir}
install fc $RPM_BUILD_ROOT%{_bindir}
install src/f2c.1t $RPM_BUILD_ROOT%{_mandir}/man1/f2c.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc f2c.ps README permission disclaimer changes src/Notice
%attr(755,root,root) %{_bindir}/f2c
%attr(755,root,root) %{_bindir}/fc
%{_mandir}/man1/f2c.1*
