Summary:	Filesystem based on the SSH File Transfer Protocol
Summary(pl.UTF-8):	System plików oparty na protokole SSH File Transfer Protocol
Name:		sshfs-fuse
Version:	3.7.5
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/libfuse/sshfs/releases
Source0:	https://github.com/libfuse/sshfs/releases/download/sshfs-%{version}/sshfs-%{version}.tar.xz
# Source0-md5:	5d9d4575d5c0b535857f41f723e92c85
URL:		https://github.com/libfuse/sshfs
BuildRequires:	docutils
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libfuse3-devel >= 3.1.0
BuildRequires:	meson >= 0.40
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libfuse3-tools >= 3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filesystem based on the SSH File Transfer Protocol.

%description -l pl.UTF-8
System plików oparty na protokole SSH File Transfer Protocol.

%prep
%setup -q -n sshfs-%{version}

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog.rst README.md
%attr(755,root,root) %{_bindir}/sshfs
%attr(755,root,root) %{_sbindir}/mount.sshfs
%attr(755,root,root) %{_sbindir}/mount.fuse.sshfs
%{_mandir}/man1/sshfs.1*
