%define name	librapi
%define release	%mkrel 5
%define version	0.11
%define major 2
%define libname %mklibname rapi %major
%define develname %mklibname -d rapi

Name:		%{name}
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		System/Libraries
Source:		%{name}%{major}-%{version}.tar.bz2
URL:		http://synce.sourceforge.net/
Buildroot:	%{_tmppath}/%name-root
BuildRequires:	libsynce-devel = %{version}
BuildRequires:	python-devel
BuildRequires:	python-pyrex
Conflicts:	synce < 0.9.3
Obsoletes:	synce-%name

%description
Librapi is part of the SynCE project.
The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC. Documentation for the RAPI calls
is available at this address:

http://msdn.microsoft.com/library/default.asp?url=/library/en-us/wcesdkr/htm/_wcesdk_CeRapiInit.asp



%package -n	%{libname}
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Obsoletes:	%libname < %libname-%{version}


%description -n %{libname}
Librapi is part of the SynCE project.



%package -n	%{libname}-python
Group:		System/Libraries
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Requires:	%{libname} = %{version}-%{release}
Requires:	python
Obsoletes:	%libname-python < %libname-python-%{version}

%description -n %{libname}-python
Librapi is part of the SynCE project.


%package -n	%{develname}
Group:		Development/C
Summary:	SynCE: Remote Application Programming Interface (RAPI) library
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{_lib}synce0-devel < 0.9.3
Obsoletes:	%libname-devel < %libname-devel-%{version}
Obsoletes:	%develname < %develname-%{version}

%description -n %{develname}
Librapi is part of the SynCE project:

%prep
%setup -q -n librapi2-%{version}

%build
%configure2_5x --with-libsynce=%{_prefix}
%make

%install
rm -rf %buildroot
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n %{libname}
%defattr(-,root,root)
%doc README TODO
%_libdir/librapi.so.%{major}
%_libdir/librapi.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%_libdir/librapi.so
%_libdir/librapi.a
%_libdir/librapi.la
%{_includedir}/rapi.h
%_libdir/pkgconfig/*.pc

%files -n %{libname}-python
%python_sitearch/pyrapi2.*
