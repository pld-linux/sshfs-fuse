Summary:	Filesystem based on the SSH File Transfer Protocol
Summary(pl.UTF-8):	System plików oparty na protokole SSH File Transfer Protocol
Name:		sshfs-fuse
Version:	2.8
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/libfuse/sshfs/releases
Source0:	https://github.com/libfuse/sshfs/releases/download/sshfs_%{version}/sshfs-%{version}.tar.gz
# Source0-md5:	0ba25e848ee59e2595d6576c8f6284b6
URL:		https://github.com/libfuse/sshfs
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libfuse-devel >= 0:2.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on the SSH File Transfer Protocol.

%description -l pl.UTF-8
System plików oparty na protokole SSH File Transfer Protocol.

%prep
%setup -q -n sshfs-%{version}

%build
%configure \
	--enable-sshnodelay
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/sshfs
%attr(755,root,root) %{_libdir}/sshnodelay.so
%{_mandir}/man1/sshfs.1*
