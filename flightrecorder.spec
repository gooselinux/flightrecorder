Name: flightrecorder
Version: 0.91
Release: 1%{?dist}
Summary: flightrecorder - runs trace-cmd to enable ftrace with predefined events

Group: Development/Tools
License: LGPLv2
URL: http://www.kernel.org/pub/linux/analysis/trace-cmd/
Source0:http://www.kernel.org/pub/linux/analysis/trace-cmd/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:
Requires: trace-cmd

%description
flightrecorder - runs trace-cmd to enable ftrace with events defined in /etc/sysconfig/trace-cmd

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
chkconfig --add trace-cmd
chkconfig --level 345 trace-cmd on
chkconfig --level 0126 trace-cmd off

%postun
chkconfig --del trace-cmd

%files
%defattr(-,root,root,-)
%{_initrddir}/*
%{_sysconfdir}/sysconfig/*
%{_sysconfdir}/logrotate.d/*

%changelog
* Thu Jul 29 2010 - John Kacur <jkacur@redhat.com>
- Fix syntax error that prevents chkconfig from working correctly

* Mon Jun 21 2010 - John Kacur <jkacur@redhat.com>
- Initial version of flightrecorder
