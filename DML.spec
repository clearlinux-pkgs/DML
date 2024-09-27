#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
Name     : DML
Version  : 1.2.0
Release  : 6
URL      : https://github.com/intel/DML/archive/v1.2.0/DML-1.2.0.tar.gz
Source0  : https://github.com/intel/DML/archive/v1.2.0/DML-1.2.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: DML-data = %{version}-%{release}
Requires: DML-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Intel® Data Mover Library (Intel® DML)
=================================================

%package data
Summary: data components for the DML package.
Group: Data

%description data
data components for the DML package.


%package dev
Summary: dev components for the DML package.
Group: Development
Requires: DML-data = %{version}-%{release}
Provides: DML-devel = %{version}-%{release}
Requires: DML = %{version}-%{release}

%description dev
dev components for the DML package.


%package license
Summary: license components for the DML package.
Group: Default

%description license
license components for the DML package.


%prep
%setup -q -n DML-1.2.0
cd %{_builddir}/DML-1.2.0
pushd ..
cp -a DML-1.2.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727475004
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DDML_BUILD_TESTS=OFF \
-DDML_BUILD_EXAMPLES=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DDML_BUILD_TESTS=OFF \
-DDML_BUILD_EXAMPLES=OFF  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1727475004
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/DML
cp %{_builddir}/DML-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/DML/d6b97f1ba83cfecb7d9dcb7165e8d5b7bdf6be98 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/DML/configs/1n1d1e1w-s-n1.conf
/usr/share/DML/configs/1n1d1e1w-s-n2.conf
/usr/share/DML/configs/1n1d4e1w-s-n1.conf
/usr/share/DML/configs/1n1d4e1w-s-n2.conf
/usr/share/DML/configs/1n2d4e1w-s-n1.conf
/usr/share/DML/configs/1n2d4e1w-s-n2.conf
/usr/share/DML/configs/1n3d4e1w-s-n1.conf
/usr/share/DML/configs/1n3d4e1w-s-n2.conf
/usr/share/DML/configs/1n4d1e1w-s-n1.conf
/usr/share/DML/configs/1n4d1e1w-s-n2.conf
/usr/share/DML/configs/1n4d4e1w-s-n1.conf
/usr/share/DML/configs/1n4d4e1w-s-n2.conf
/usr/share/DML/configs/2n1d1e1w-s.conf
/usr/share/DML/configs/2n1d4e1w-s.conf
/usr/share/DML/configs/2n2d4e1w-s.conf
/usr/share/DML/configs/2n3d4e1w-s.conf
/usr/share/DML/configs/2n4d4e1w-s.conf
/usr/share/DML/scripts/accel_conf.py
/usr/share/DML/scripts/accel_conf.sh

%files dev
%defattr(-,root,root,-)
/usr/include/dml/detail/common/flags.hpp
/usr/include/dml/detail/common/specific_flags.hpp
/usr/include/dml/detail/common/status.hpp
/usr/include/dml/detail/common/types.hpp
/usr/include/dml/detail/common/utils/enum.hpp
/usr/include/dml/detail/ml/allocator.hpp
/usr/include/dml/detail/ml/buffer.hpp
/usr/include/dml/detail/ml/execution_path.hpp
/usr/include/dml/detail/ml/impl/core_interconnect.hpp
/usr/include/dml/detail/ml/impl/make_descriptor.hpp
/usr/include/dml/detail/ml/make_task.hpp
/usr/include/dml/detail/ml/options.hpp
/usr/include/dml/detail/ml/result.hpp
/usr/include/dml/detail/ml/task.hpp
/usr/include/dml/detail/ml/utils.hpp
/usr/include/dml/detail/ml/view.hpp
/usr/include/dml/dml.h
/usr/include/dml/dml.hpp
/usr/include/dml/dmldefs.h
/usr/include/dml/hl/data_view.hpp
/usr/include/dml/hl/detail/buffer.hpp
/usr/include/dml/hl/detail/execute.hpp
/usr/include/dml/hl/detail/handler.hpp
/usr/include/dml/hl/detail/make_result.hpp
/usr/include/dml/hl/detail/submit.hpp
/usr/include/dml/hl/detail/utils.hpp
/usr/include/dml/hl/execute.hpp
/usr/include/dml/hl/execution_interface.hpp
/usr/include/dml/hl/execution_path.hpp
/usr/include/dml/hl/handler.hpp
/usr/include/dml/hl/operations.hpp
/usr/include/dml/hl/result.hpp
/usr/include/dml/hl/sequence.hpp
/usr/include/dml/hl/status_code.hpp
/usr/include/dml/hl/submit.hpp
/usr/include/dml/hl/types.hpp
/usr/lib64/cmake/DML/DMLConfig.cmake
/usr/lib64/cmake/DML/DMLConfigVersion.cmake
/usr/lib64/cmake/DML/DMLTargets-relwithdebinfo.cmake
/usr/lib64/cmake/DML/DMLTargets.cmake

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/DML/d6b97f1ba83cfecb7d9dcb7165e8d5b7bdf6be98
