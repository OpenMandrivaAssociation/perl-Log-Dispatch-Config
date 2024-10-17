%define upstream_name    Log-Dispatch-Config
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Log4j for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Log/Dispatch*
%{_mandir}/*/*


%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 654093
- update to new version 1.04

* Fri Feb 05 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 501144
- update to 1.03
- fixed url field

* Thu Jul 23 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 398793
- rebuild
- using %%perl_convert_version
- fixed summary, license, buildrequires fields

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.02-3mdv2009.0
+ Revision: 241649
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 09 2007 Funda Wang <fwang@mandriva.org> 1.02-1mdv2008.0
+ Revision: 60693
- New version 1.02


* Tue Sep 27 2005 Oden Eriksson <oeriksson@mandriva.com> 1.01-6mdk
- fix deps
- run the test suite

* Mon Jan 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.01-5mdk
- use requires_exceptions

* Tue Aug 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.01-4mdk
- rebuild
- use %%makeinstall_std macro
- don't set PREFIX
- use %%make macro
- drop $RPM_OPT_FLAGS, no need

* Wed Aug 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.01-3mdk
- rebuild

* Mon Jun 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.01-2mdk
- from Peter Chen <petechen@86.private> :
	- Remove blank line from description.

* Thu Jun 13 2002 Peter Chen <petechen@netilla.com> 1.01-1mdk
- 1.01

