# Do not package empty debug_package
%global debug_package %{nil}

Summary: Nethserver arm configuration
Name: nethserver-arm-extra-config
Version: 1.1.2
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz

BuildRequires: nethserver-devtools

%description
Nethserver arm configuration

%prep
%setup -q

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog

* Wed Jan 13 2021 Mark Verlinde <mark.verlinde@gmail.com> - 1.1.2
- to keep network running and optain a IP from DHCP NM is stopped after system int
- preset Networkmanager-wait-online is not stop, force stop of all units

* Mon Jan 04 2021 Mark Verlinde <mark.verlinde@gmail.com> - 1.1.1
- Disable NetworkManger and other (well-known) services at the end of system-init,

* Wed Dec 23 2020 Mark Verlinde <mark.verlinde@gmail.com> - 1.1.0
- Disable NetworkManger and other (well-known) services during system-init,
  NetworkManger and NetworkManger-wait-online are enbaled on fist-boot

* Sat May 16 2020 Mark Verlinde <mark.verlinde@gmail.com> - 1.0.0
- Extended template expansion of /etc/nethserver/eorepo.conf
  part of nethserver-base fixes, arm-dev #40

* Fri May 15 2020 Mark Verlinde <mark.verlinde@gmail.com> - 0.1.1
- First (unreleased) rpm-build