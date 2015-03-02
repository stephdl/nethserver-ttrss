# Authority: vip-ire
# Name: Daniel Berteaud

%define name smeserver-tt-rss
%define version 0.2.8
%define release 1
Summary: sme server integration of tt-rss
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://www.zabbix.com/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz

BuildArchitectures: noarch
BuildRequires: e-smith-devtools
BuildRoot: /var/tmp/%{name}-%{version}
Requires: e-smith-release
Requires: tt-rss >= 1.7.9
Requires: smeserver-webapps-common
AutoReqProv: no

%description
smserver integration of TIny Tiny RSS
Tiny Tiny RSS is a feature rich, web based feed reader

%changelog
* Thu Feb 6 2014 Daniel Berteaud <daniel@firewall-services.com> 0.2.8-1.sme
- Fix database upgrades

* Mon Jan 20 2014 Daniel Berteaud <daniel@firewall-services.com> 0.2.7-1.sme
- Remove the default Authentication prop (but the default value is still http)

* Wed Dec 18 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.6-1.sme
- Add DETECT_ARTICLE_LANGUAGE, for tt-rss 1.11
- Automatically update database schema when needed

* Wed Jun 12 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.5-1.sme
- Add SMTP_SECURE, for tt-rss 1.8

* Tue May 14 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.4-1.sme
- Support tt-rss 1.7.9

* Sun Mar 24 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.3-1.sme
- update daemon run script to use --daemon argument

* Sat Mar 23 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.2-1.sme
- Add missing SMTP_PORT

* Tue Mar 5 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.1-1.sme
- Support tt-rss 1.7.1

* Wed Nov 14 2012 Daniel Berteaud <daniel@firewall-services.com> 0.2.0-1.sme
- Support tt-rss 1.6.1

* Tue Apr 24 2012 Daniel Berteaud <daniel@firewall-services.com> 0.1.0-1.sme
- Migrate to GIT

* Fri Nov 25 2011 Daniel Berteaud <daniel@firewall-services.com> 0.1-8.sme
- Define SELF_URL_PATH in config
- Update config version to 23 (1.5.7)

* Mon Jul 25 2011 Daniel Berteaud <daniel@firewall-services.com> 0.1-7.sme
- Configure cache dir (prevent log noise)

* Tue Jun 07 2011 Daniel B. <daniel@firewall-services.com> 0.1-6.sme
- MySQL schema files are not doc files anymore

* Tue May 17 2011 Daniel B. <daniel@firewall-services.com> 0.1-5
- Deny access to the /schema directory

* Wed Jan 26 2011 Daniel B. <daniel@firewall-services.com> 0.1-4
- Add DB_PORT param in config file

* Wed Jan 26 2011 Daniel B. <daniel@firewall-services.com> 0.1-3
- Support tt-rss 1.5.1

* Mon Jan 03 2011 Daniel B. <daniel@firewall-services.com> 0.1-2
- disable cron job, as feeds are updated via the daemon

* Mon Jan 03 2011 Daniel B. <daniel@firewall-services.com> 0.1-1
- initial release

%prep
%setup
%build
perl ./createlinks
%{__mkdir_p} root/var/log/tt-rss

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  --file /var/service/tt-rss/run 'attr(0755,root,root)' \
  --file /var/service/tt-rss/log/run 'attr(0755,root,root)' \
  --dir /var/log/tt-rss 'attr(0770,root,smelog)' \
  > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT

%postun

