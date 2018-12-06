#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lchown
Version  : 1.01
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/N/NC/NCLEATON/Lchown-1.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NC/NCLEATON/Lchown-1.01.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblchown-perl/liblchown-perl_1.01-3.debian.tar.xz
Summary  : use the lchown(2) system call from Perl
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Lchown-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Lchown - perl interface to the lchown(2) system call
The Lchown module provides a perl interface to the lchown(2) UNIX system
call, on systems that support lchown.  The lchown(2) call is used to
change the ownership and group of symbolic links.

%package dev
Summary: dev components for the perl-Lchown package.
Group: Development
Requires: perl-Lchown-lib = %{version}-%{release}
Provides: perl-Lchown-devel = %{version}-%{release}

%description dev
dev components for the perl-Lchown package.


%package lib
Summary: lib components for the perl-Lchown package.
Group: Libraries

%description lib
lib components for the perl-Lchown package.


%prep
%setup -q -n Lchown-1.01
cd ..
%setup -q -T -D -n Lchown-1.01 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Lchown-1.01/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Lchown.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lchown.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Lchown/Lchown.so
