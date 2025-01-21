#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lchown
Version  : 1.01
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/N/NC/NCLEATON/Lchown-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NC/NCLEATON/Lchown-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblchown-perl/liblchown-perl_1.01-3.debian.tar.xz
Summary  : use the lchown(2) system call from Perl
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Lchown-license = %{version}-%{release}
Requires: perl-Lchown-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Lchown - perl interface to the lchown(2) system call
The Lchown module provides a perl interface to the lchown(2) UNIX system
call, on systems that support lchown.  The lchown(2) call is used to
change the ownership and group of symbolic links.

%package dev
Summary: dev components for the perl-Lchown package.
Group: Development
Provides: perl-Lchown-devel = %{version}-%{release}
Requires: perl-Lchown = %{version}-%{release}

%description dev
dev components for the perl-Lchown package.


%package license
Summary: license components for the perl-Lchown package.
Group: Default

%description license
license components for the perl-Lchown package.


%package perl
Summary: perl components for the perl-Lchown package.
Group: Default
Requires: perl-Lchown = %{version}-%{release}

%description perl
perl components for the perl-Lchown package.


%prep
%setup -q -n Lchown-1.01
cd %{_builddir}
tar xf %{_sourcedir}/liblchown-perl_1.01-3.debian.tar.xz
cd %{_builddir}/Lchown-1.01
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Lchown-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Lchown
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Lchown/8fcb670a0a8dea3cc1801dc64f0025b99c2be5f6
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lchown.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Lchown/8fcb670a0a8dea3cc1801dc64f0025b99c2be5f6

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
