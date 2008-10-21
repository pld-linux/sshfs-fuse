Summary:	Filesystem based on the SSH File Transfer Protocol
Summary(pl.UTF-8):	System plików oparty na protokole SSH File Transfer Protocol
Name:		sshfs-fuse
Version:	2.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fuse/%{name}-%{version}.tar.gz
# Source0-md5:	26e9206eb5169e87e6f95f54bc005a4f
URL:		http://fuse.sourceforge.net/sshfs.html
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libfuse-devel >= 0:2.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on the SSH File Transfer Protocol.

%description -l pl.UTF-8
System plików oparty na protokole SSH File Transfer Protocol.

%prep
%setup -q

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/sshfs
%attr(755,root,root) %{_libdir}/sshnodelay.so
%{_mandir}/man1/sshfs.1*
