%define major		2
%define libname		%mklibname rapi %{major}
%define develname	%mklibname -d rapi
%define svn	0

Name:		librapi
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Version:	0.15.2
Release:	4
License:	MIT
Group:		System/Libraries
URL:		https://synce.sourceforge.net/
Source0:	%{name}%{major}-%{version}.tar.gz
Patch0:		librapi2-dso.patch
BuildRequires:	libsynce-devel >= 0.15.1
BuildRequires:	python-devel
BuildRequires:	python-pyrex

%description
Librapi is part of the SynCE project.
The RAPI library is an open source implementation that works like
RAPI.DLL, available on Microsoft operating systems. The library makes
it possible to make remote calls to a computer running Pocket PC.
Documentation for the RAPI calls is available at this address:

http://goo.gl/nsCoA

%package -n	%{libname}
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library

%description -n %{libname}
Librapi is part of the SynCE project. This package contains shared
libraries.

%package -n	%{name}-python
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Requires:	%{libname} = %{version}-%{release}
Requires:	python

%description -n %{name}-python
Librapi is part of the SynCE project. This package contains Python
bindings.

%package -n	%{develname}
Group:		Development/C
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Librapi is part of the SynCE project. This package contains development
headers.

%prep
%setup -q -n %{name}2-%{version}
%patch0 -p0

%build
%configure2_5x --disable-static --disable-rpath --enable-udev-support --disable-hal-support
%make

%install
%makeinstall_std

rm -f %{buildroot}%{python_sitearch}/pyrapi2.{la,a}

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%doc README TODO
%{_libdir}/%{name}.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc

%files -n %{name}-python
%{py_platsitedir}/pyrapi2.*



%changelog
* Tue Mar 15 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.15.2-1mdv2011.0
+ Revision: 645049
- new version 0.15.2
  disabled hal support and enabled udev support

* Sat Nov 13 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 0.15-2mdv2011.0
+ Revision: 597033
- rebuild for python 2.7

* Tue Apr 27 2010 Emmanuel Andry <eandry@mandriva.org> 0.15-1mdv2010.1
+ Revision: 539630
- New version 0.15

* Thu Mar 04 2010 Emmanuel Andry <eandry@mandriva.org> 0.15-0.r3893.1mdv2010.1
+ Revision: 514173
- pre 0.15 svn snapshot

* Thu Jul 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.0
+ Revision: 398828
- Add some BuildRequires needed for autoreconf
- Update to new version 0.14
- Don't remove -Werror from CFLAGS because it results in broken
  CFLAGS if you use "Werror=format-security"
- Don't build static libraries
- Remove rpath
- Use fixed version number in obsoletes so that not more and more
  unexisting versions are obsoleted

* Tue Jan 13 2009 Adam Williamson <awilliamson@mandriva.org> 0.13.1-1mdv2009.1
+ Revision: 329177
- hack up the synce br because of the non-synced releases
- drop nogil.diff (merged upstream)
- new release 0.13.1

* Mon Jan 12 2009 Adam Williamson <awilliamson@mandriva.org> 0.13-1mdv2009.1
+ Revision: 328728
- add pyrapi-nogil.diff: fix build with recent pyrex (from Mark Ellis)
- new release 0.13

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.12-2mdv2009.1
+ Revision: 319650
- rebuild with python 2.6

* Wed Jul 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.12-1mdv2009.0
+ Revision: 236629
- new release 0.12

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Adam Williamson <awilliamson@mandriva.org> 0.11.1-1mdv2009.0
+ Revision: 194613
- drop all patches (merged upstream)
- new release 0.11.1

* Thu Mar 20 2008 Adam Williamson <awilliamson@mandriva.org> 0.11-9mdv2008.1
+ Revision: 189196
- add timeout.patch: from upstream SVN, increases a timeout (avoids problems when removing larger applications)

* Wed Mar 12 2008 Adam Williamson <awilliamson@mandriva.org> 0.11-8mdv2008.1
+ Revision: 187221
- streamline file lists
- python package should be %%{name}-python not %%{libname}-python
- move docs from lib to devel package, add conflicts to ensure successful upgrade
- add rapierror.patch (RAPIError must be a subclass of Exception - needed to fix a bug in sync-engine)
- version all obsoletes
- Clean up spec (tabs, macros, descriptions)

* Fri Feb 01 2008 Funda Wang <fwang@mandriva.org> 0.11-7mdv2008.1
+ Revision: 161182
- correctly obsoletes old devel package

* Mon Jan 14 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-6mdv2008.1
+ Revision: 151760
- add provides

* Sat Jan 12 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-5mdv2008.1
+ Revision: 149804
- fix obsoletes again

* Fri Jan 11 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-4mdv2008.1
+ Revision: 149175
- split binaries into a separate package
- fix obsoletes

* Thu Jan 10 2008 Emmanuel Andry <eandry@mandriva.org> 0.11-2mdv2008.1
+ Revision: 147736
- import librapi


