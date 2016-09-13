Name:       libngf-qt
Summary:    Qt-based client library for Non-Graphic Feedback daemon
Version:    0.2
Release:    1
Group:      System/Libraries
License:    LGPLv2.1
URL:        https://github.com/nemomobile/libngf-qt
Source0:    %{name}-%{version}.tar.bz2
Source100:  libngf-qt.yaml
Requires:   ngfd
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  pkgconfig(QtTest)
BuildRequires:  doxygen

%description
This package contains the Qt-based client library for accessing
Non-graphic feedback services.


%package devel
Summary:    Development package for Qt-based client library for NGF daemon
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package declarative
Summary:    Declarative plugin for NGF clients
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description declarative
%{summary}.

%package tests
Summary:    Test suite for libngf-qt
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}


%build
%qmake 

make %{?jobs:-j%jobs}

make doc

%install
rm -rf %{buildroot}
%qmake_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libngf-qt.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libngf-qt.so
%{_includedir}/ngf-qt/*.h
%{_includedir}/ngf-qt/NgfClient
%{_libdir}/pkgconfig/ngf-qt.pc

%files declarative
%defattr(-,root,root,-)
%{_libdir}/qt4/imports/org/nemomobile/ngf/*

%files tests
%defattr(-,root,root,-)
/opt/tests/libngf-qt/*
