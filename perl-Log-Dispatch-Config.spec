%define upstream_name    Log-Dispatch-Config
%define upstream_version 1.03

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary: 	Log4j for Perl
License: 	GPL+ or Artistic
Group: 		Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}/
Source0: 	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::Simple)  >= 0.420.0
BuildRequires: perl(AppConfig)     >= 1.520.0
BuildRequires: perl(IO::Stringy)
BuildRequires: perl(Log::Dispatch) >= 2.110.0

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description 
Log::Dispatch::Config is a subclass of Log::Dispatch and provides a way
to configure Log::Dispatch object with configulation file (default, in
AppConfig format). I mean, this is log4j for Perl, not with all API
compatibility though.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/Dispatch*
%{_mandir}/*/*
