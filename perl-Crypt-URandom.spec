#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Crypt
%define		pnam	URandom
Summary:	Crypt::URandom - Provide non blocking randomness
Summary(pl.UTF-8):	Crypt::URandom - nieblokująca losowość
Name:		perl-Crypt-URandom
Version:	0.54
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	011113679de05d1c2bea37fe92f60278
URL:		https://metacpan.org/dist/Crypt-URandom
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended to provide an interface to the strongest
available source of non-blocking randomness on the current platform.
Platforms currently supported are anything supporting getrandom(2),
/dev/urandom and versions of Windows greater than or equal to Windows
2000.

%description -l pl.UTF-8
Celem tego modułu jest udostępnienie interfejsu do najsilniejszego
dostępnego źródła nieblokującej losowości na bieżącej platformie.
Obecnie obsługiwane są wszystkie obsługujące getrandom(2),
/dev/urandom oraz Windows począwszy od wersji 2000.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/URandom.pm
%dir %{perl_vendorarch}/auto/Crypt/URandom
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/URandom/URandom.so
%{_mandir}/man3/Crypt::URandom.3pm*
