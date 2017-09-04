Summary: Decodes MS-TNEF attachments.
Name: tnef
Version: 1.4.15
Release: 1
Group: Mail/Encoders
Copyright: GPL
Source: http://world.std.com/~damned/tnef-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: /usr/local
Vendor: Angst Programming I.G.
URL: http://tnef.sourceforge.net
Packager: Mark Simpson <verdammelt@gmail.com>

%description
TNEF is a program for unpacking MIME attachments of type
"application/ms-tnef". This is a Microsoft only attachment.

Due to the proliferation of Microsoft Outlook and Exchange mail servers,
more and more mail is encapsulated into this format.

The TNEF program allows one to unpack the attachments which were
encapsulated into the TNEF attachment.  Thus alleviating the need to use
Microsoft Outlook to view the attachment.


%prep
%setup

%build
CFLAGS=${RPM_OPT_FLAGS} ./configure --prefix=%{prefix} --datarootdir=%{prefix}/share
make all

%install
make "DESTDIR=${RPM_BUILD_ROOT}" install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc README.md COPYING ChangeLog AUTHORS NEWS TODO BUGS
%{prefix}/bin/tnef
%{prefix}/share/man/man1/tnef.1.gz

