%define module  Log-Dispatch-Config
%define version 1.01
%define release 6mdk
%define	pdir	Log

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group: 		Development/Perl
URL:            http://search.cpan.org/search?dist=%{module}
Source0: 	%{module}-%{version}.tar.bz2
BuildArch: 	noarch
BuildRequires:	perl-devel perl-Test-Simple >= 0.42 perl-AppConfig >= 1.52
BuildRequires:	perl-IO-stringy perl-Log-Dispatch >= 2.11-2mdk
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description 
%{module} module for perl.  Log::Dispatch::Config is a subclass of
Log::Dispatch and provides a way to configure Log::Dispatch object
with configulation file (default, in AppConfig format). I mean, this
is log4j for Perl, not with all API compatibility though.

%prep
%setup -q -n %{module}-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

make test

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

