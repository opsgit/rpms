# $Id$
# Authority: dag
# Upstream: Dan Kogai <dankogai$dan,co,jp>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-which

Summary: Perl module to tell fully qualified name of the method
Name: perl-UNIVERSAL-which
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-which/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-which-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UNIVERSAL-which is a Perl module to tell fully qualified name
of the method.

This package contains the following Perl module:

    UNIVERSAL::which

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/UNIVERSAL::which.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
#%{perl_vendorlib}/UNIVERSAL/which/
%{perl_vendorlib}/UNIVERSAL/which.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
