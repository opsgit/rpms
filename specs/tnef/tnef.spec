# $Id$
# Authority: dag

Summary: Unpack Microsoft MS-TNEF MIME attachements
Name: tnef
Version: 1.3.2
Release: 1
License: GPL
Group: Applications/File
URL: http://sourceforge.net/projects/tnef/

Source: http://dl.sf.net/tnef/tnef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gawk

%description
TNEF provides a way to unpack those pesky Microsoft MS-TNEF MIME
attachments. It operates like tar in order to upack any files
which may have been put into the MS-TNEF attachment instead of
being attached seperately.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc %{_mandir}/man1/tnef.1*
%{_bindir}/tnef

%changelog
* Tue Apr 05 2005 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Initial package. (using DAR)
