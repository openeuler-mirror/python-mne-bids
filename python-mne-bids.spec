%global _empty_manifest_terminate_build 0
Name:		python-mne-bids
Version:	0.9
Release:	1
Summary:	Organizing MEG, EEG, and iEEG data according to the BIDS specification and facilitating their analysis with MNE-Python
License:	BSD-3-Clause
URL:		https://github.com/mne-tools/mne-bids
Source0:	https://files.pythonhosted.org/packages/a0/f2/1091a5e4e89746105577a8d00bf8ac1063f847f7363d8120a4d1d5d022e5/mne-bids-0.9.tar.gz
BuildArch:	noarch

Requires:	python3-mne
Requires:	python3-numpy
Requires:	python3-scipy
Requires:	python3-setuptools
Requires:	python3-nibabel
Requires:	python3-pybv
Requires:	python3-matplotlib
Requires:	python3-pandas
Requires:	python3-openneuro-py
Requires:	python3-EDFlib-Python

%description
MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.

%package -n python3-mne-bids
Summary:	Organizing MEG, EEG, and iEEG data according to the BIDS specification and facilitating their analysis with MNE-Python
Provides:	python-mne-bids
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%description -n python3-mne-bids
MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.

%package help
Summary:	Development documents and examples for mne-bids
Provides:	python3-mne-bids-doc
%description help
MNE-BIDS is a Python package that allows you to read and write BIDS-compatible datasets with the help of MNE-Python.

%prep
%autosetup -n mne-bids-0.9

%build
%py3_build

%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
	find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
	find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
	find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
	find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
	find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%files -n python3-mne-bids -f filelist.lst
%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Dec 17 2021 Python_Bot <Python_Bot@openeuler.org> - 0.9-1
- Package Init

