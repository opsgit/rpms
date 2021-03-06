# $Id$
# Authority: dag

%define real_name drupal

Summary: Drupal CMS
Name: drupal6
Version: 6.25
Release: 1%{?dist}
License: GPL
Group: Development/Languages
URL: http://drupal.org/

Source: http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: php >= 4.3.5
Requires: httpd, mysql, php >= 4.3.5
Requires: php-gd, php-mbstring, php-mysql

Obsoletes: drupal <= %{version}-%{release}
Provides: drupal = %{version}-%{release}

%description
Drupal is an open source content management platform. Drupal is equipped
with a powerful blend of features, Drupal can support a variety of
websites ranging from personal weblogs to large community-driven websites.

%prep
%setup -n %{real_name}-%{version}
%{__cat} <<EOF >drupal6.httpd
### Drupal 6
Alias /drupal %{_localstatedir}/www/drupal-%{version}

<Directory %{_localstatedir}/www/drupal-%{version}>
    AllowOverride All
</Directory>
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 drupal6.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/drupal6.conf
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/drupal-%{version}/files/
%{__install} -Dp -m0644 .htaccess %{buildroot}%{_localstatedir}/www/drupal-%{version}/.htaccess
%{__cp} -av *.php %{buildroot}%{_localstatedir}/www/drupal-%{version}/
%{__cp} -av includes/ misc/ modules/ profiles/ scripts/ sites/ themes/ %{buildroot}%{_localstatedir}/www/drupal-%{version}/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, apache, apache, 0755)
%doc CHANGELOG.txt INSTALL.mysql.txt INSTALL.pgsql.txt INSTALL.txt LICENSE.txt MAINTAINERS.txt UPGRADE.txt
%config(noreplace) %{_localstatedir}/www/drupal-%{version}/sites/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/drupal6.conf
%{_localstatedir}/www/drupal-%{version}/

%changelog
* Sun Mar 11 2012 Dag Wieers <dag@wieers.com> - 6.25-1
- Updated to release 6.25.

* Sun Aug 22 2010 Dag Wieers <dag@wieers.com> - 6.19-1
- Updated to release 6.19.

* Thu Jun 10 2010 Dag Wieers <dag@wieers.com> - 6.17-1
- Updated to release 6.17.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 6.16-1
- Updated to release 6.16.

* Tue Dec 29 2009 Christoph Maser <cmr@financial.com> - 6.15-1
- Updated to version 6.15.

* Sun Sep 27 2009 Dag Wieers <dag@wieers.com> - 6.14-1
- Updated to release 6.14.

* Thu Jul 02 2009 Dag Wieers <dag@wieers.com> - 6.13-1
- Updated to release 6.13.

* Sun May 17 2009 Dag Wieers <dag@wieers.com> - 6.12-1
- Updated to release 6.12.

* Mon May 11 2009 Dag Wieers <dag@wieers.com> - 6.11-1
- Updated to release 6.11.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 6.9-1
- Updated to release 6.9.

* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 6.8-1
- Updated to release 6.8.

* Fri Jun 13 2008 Dag Wieers <dag@wieers.com> - 6.2-1
- Updated to release 6.2.

* Thu Feb 28 2008 Dag Wieers <dag@wieers.com> - 6.1-1
- Updated to release 6.1.

* Fri Feb 15 2008 Dag Wieers <dag@wieers.com> - 6.0-1
- Initial package. (using DAR)
