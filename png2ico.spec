%define date 2002-12-08

Summary:	PNG to icon converter
Name:		png2ico
Version:	20021208
Release:	15
License:	GPLv2+
Group:		Graphics
Url:		https://www.winterdrache.de/freeware/png2ico/index.html
Source0:	http://www.winterdrache.de/freeware/png2ico/data/%{name}-src-%{date}.tar.bz2
Patch0:		png2ico-20021208-gcc49.patch
BuildRequires:	pkgconfig(libpng)

%description
Converts PNG files to Windows icon resource files. If you're looking
for a program to create a favicon.ico for your website, look no
further. If you need instructions or don't even know what a favicon is,
check out this short tutorial on how to create and install a favicon.ico
http://www.winterdrache.de/freeware/png2ico/favicon.html

%files
%doc LICENSE VERSION README README.unix doc/bmp.txt
%{_bindir}/*
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -n %{name}
%patch0 -p1

%build
make CPPFLAGS="%{optflags}"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1


