#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-altgraph
Version  : 0.17.2
Release  : 4
URL      : https://files.pythonhosted.org/packages/a9/f1/62830c4915178dbc6948687916603f1cd37c2c299634e4a8ee0efc9977e7/altgraph-0.17.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a9/f1/62830c4915178dbc6948687916603f1cd37c2c299634e4a8ee0efc9977e7/altgraph-0.17.2.tar.gz
Summary  : Python graph (network) package
Group    : Development/Tools
License  : MIT
Requires: pypi-altgraph-license = %{version}-%{release}
Requires: pypi-altgraph-python = %{version}-%{release}
Requires: pypi-altgraph-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
altgraph is a fork of graphlib: a graph (network) package for constructing
graphs, BFS and DFS traversals, topological sort, shortest paths, etc. with
graphviz output.

%package license
Summary: license components for the pypi-altgraph package.
Group: Default

%description license
license components for the pypi-altgraph package.


%package python
Summary: python components for the pypi-altgraph package.
Group: Default
Requires: pypi-altgraph-python3 = %{version}-%{release}

%description python
python components for the pypi-altgraph package.


%package python3
Summary: python3 components for the pypi-altgraph package.
Group: Default
Requires: python3-core
Provides: pypi(altgraph)

%description python3
python3 components for the pypi-altgraph package.


%prep
%setup -q -n altgraph-0.17.2
cd %{_builddir}/altgraph-0.17.2
pushd ..
cp -a altgraph-0.17.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656355204
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-altgraph
cp %{_builddir}/altgraph-0.17.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-altgraph/5b3c3863d521cf35e75e36a22e5ec4a80c93c528
cp %{_builddir}/altgraph-0.17.2/doc/license.rst %{buildroot}/usr/share/package-licenses/pypi-altgraph/5c8cb37144bd49eb123da1cf3b7b2d098d155a80
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-altgraph/5b3c3863d521cf35e75e36a22e5ec4a80c93c528
/usr/share/package-licenses/pypi-altgraph/5c8cb37144bd49eb123da1cf3b7b2d098d155a80

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
