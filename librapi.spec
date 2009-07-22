%define major		2
%define libname		%mklibname rapi %major
%define develname	%mklibname -d rapi

Name:		librapi
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Version:	0.14
Release:	%{mkrel 1}
License:	MIT
Group:		System/Libraries
Source0:	%{name}%{major}-%{version}.tar.gz
# Don't simply remove -Werror from CFLAGS, because it results in broken
# "=format-security" CFLAG on Mandriva
Patch0:		librapi2-0.14-configure.patch
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	libsynce-devel 
BuildRequires:	python-devel
BuildRequires:	python-pyrex
Conflicts:	synce < 0.9.3
Obsoletes:	synce-%{name} < 0.13

%description
Librapi is part of the SynCE project.
The RAPI library is an open source implementation that works like
RAPI.DLL, available on Microsoft operating systems. The library makes
it possible to make remote calls to a computer running Pocket PC.
Documentation for the RAPI calls is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp

%package -n	%{libname}
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Conflicts:	%{mklibname -d rapi} < 0.11-8mdv2008.1

%description -n %{libname}
Librapi is part of the SynCE project. This package contains shared
libraries.

%package -n	%{name}-python
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Requires:	%{libname} = %{version}-%{release}
Requires:	python
Obsoletes:	%{mklibname rapi 2}-python <= 0.13

%description -n %{name}-python
Librapi is part of the SynCE project. This package contains Python
bindings.

%package -n	%{develname}
Group:		Development/C
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}synce0-devel < 0.9.3
Conflicts:	%{mklibname rapi 2} < 0.11-8mdv2008.1
Obsoletes:	%mklibname -d rapi 2 <= 0.13

%description -n %{develname}
Librapi is part of the SynCE project. This package contains development
headers.

%prep
%setup -q -n librapi2-%{version}
%patch0 -p1 -b .conf

%build
# needed for patch0
autoreconf -fis
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.{la,a}
rm -f %{buildroot}%{python_sitearch}/pyrapi2.{la,a}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README TODO
%{_libdir}/%{name}.so
%{_includedir}/rapi.h
%{_libdir}/pkgconfig/*.pc

%files -n %{name}-python
%{py_platsitedir}/pyrapi2.*

