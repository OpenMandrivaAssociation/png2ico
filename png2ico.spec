%define name	png2ico
%define version	20021208
%define date	2002-12-08
%define release	%mkrel 7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PNG to icon converter
Source:		http://www.winterdrache.de/freeware/png2ico/data/%{name}-src-%{date}.tar.bz2
URL:		http://www.winterdrache.de/freeware/png2ico/index.html
License:	GPL
Group:		Graphics
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Converts PNG files to Windows icon resource files. If you're looking
for a program to create a favicon.ico for your website, look no
further. If you need instructions or don't even know what a favicon is,
check out this short tutorial on how to create and install a favicon.ico
 http://www.winterdrache.de/freeware/png2ico/favicon.html

%prep
rm -rf %{buildroot}
%setup -n %{name}

%build
make CPPFLAGS="%{optflags}"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE VERSION README README.unix doc/bmp.txt
%{_bindir}/*
%{_mandir}/man1/*

