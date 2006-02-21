Summary:	Filesystem based on the SSH File Transfer Protocol
Summary(pl):	System plików oparty na protokole SSH File Transfer Protocol
Name:		sshfs-fuse
Version:	1.5
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/fuse/%{name}-%{version}.tar.gz
# Source0-md5:	4a376247721c3615a29ee0b2ab39619b
Patch0:		%{name}-fPIC.patch
URL:		http://fuse.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libfuse-devel >= 0:2.5
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on the SSH File Transfer Protocol.

%description -l pl
System plików oparty na protokole SSH File Transfer Protocol.

%prep
%setup -q
%patch0 -p1

%build
%configure
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
