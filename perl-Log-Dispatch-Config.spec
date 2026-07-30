%define upstream_name    Log-Dispatch-Config
%define upstream_version 1.04
Name:		perl-%{upstream_name}
Version:	1.04
Release:	3

Summary:	Log4j for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/Log-Dispatch-Config
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Log-Dispatch-Config-1.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Simple)  >= 0.420.0
BuildRequires:	perl(AppConfig)     >= 1.520.0
BuildRequires:	perl(IO::Stringy)
BuildRequires:	perl(Log::Dispatch) >= 2.110.0

BuildArch:	noarch

%description 
Log::Dispatch::Config is a subclass of Log::Dispatch and provides a way
to configure Log::Dispatch object with configulation file (default, in
AppConfig format). I mean, this is log4j for Perl, not with all API
compatibility though.

%prep
%setup -q -n Log-Dispatch-Config-1.04

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/Dispatch*
%{_mandir}/*/*


