Summary:	The f2c Fortran to C/C++ conversion program and libraries
Summary(pl):	Program f2c do t³umaczenia z Fortranu na C/C++ i biblioteki
Name:		f2c
Version:	20031027
Release:	1
License:	Distributable
Group:		Development/Languages/Fortran
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	bcd2c9ba1307c9fc9f73027c3c4e3d4c
Patch0:		%{name}-20031027.patch
URL:		ftp://ftp.netlib.org/f2c/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
f2c converts Fortran 77 source code to C or C++ source files. If no
Fortran files are named on the command line, f2c can read Fortran from
standard input and write C to standard output.

f2c can also be used (with the -P option) to generate ANSI C header
files for calling Fortran routines from C.

%description -l pl
f2c s³u¿y do t³umaczenia kodu ¼ród³owego w Fortranie 77 na kod
dj±c w wyniku pliki z kodem ¼ród³owym w C lub C++. Je¶li w wierszu
polecenia nie zostan± podane ¿adne pliki, f2c bêdzie oczekiwa³ kodu w
Fortranie na standardowym wej¶ciu i pisa³ kod w C na standardowe
wyj¶cie.

f2c mo¿e równie¿ s³u¿yæ (z opcj± -P) do generowania plików
nag³ówkowych ANSI C w celu wywo³ywania procedur Fortranowskich z C.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1

%build
%ifarch alpha
MFLAG=-mieee
%endif

mkdir -p $RPM_BUILD_DIR/f2c-%{version}/libf2c/PIC

cp -f libf2c/makefile.u libf2c/Makefile
cp -f src/makefile.u src/Makefile
make -C src RPM_OPT_FLAGS="$RPM_OPT_FLAGS" MFLAG="$MFLAG" f2c
make -C libf2c RPM_OPT_FLAGS="$RPM_OPT_FLAGS" MFLAG="$MFLAG" 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1 $RPM_BUILD_ROOT/%{_libdir} $RPM_BUILD_ROOT/%{_includedir} 
install libf2c/libf2c.a $RPM_BUILD_ROOT/%{_libdir}
install f2c.h $RPM_BUILD_ROOT/%{_includedir}
install src/f2c $RPM_BUILD_ROOT/%{_bindir}
install fc $RPM_BUILD_ROOT/%{_bindir}
install src/f2c.1t $RPM_BUILD_ROOT/%{_mandir}/man1/f2c.1
install libf2c/libf2c.so.0.22 $RPM_BUILD_ROOT/%{_libdir}
ln -sf %{_libdir}/libf2c.so.0.22 $RPM_BUILD_ROOT/%{_libdir}libf2c.so

rm -rf $RPM_BUILD_ROOT/%{_prefix}/liblibf2c.so
 
%post	-p /sbin/ldconfig

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc f2c.ps README permission disclaimer changes src/Notice
%{_libdir}/*
%{_includedir}/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT
