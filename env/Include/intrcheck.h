
#ifndef Py_INTRCHECK_H
#define Py_INTRCHECK_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) PSellerOrBuyerS_InterruptOccurred(void);
PyAPI_FUNC(void) PSellerOrBuyerS_InitInterrupts(void);
#ifdef HAVE_FORK
#if !defined(Py_LIMITED_API) || Py_LIMITED_API+0 >= 0x03070000
PyAPI_FUNC(void) PSellerOrBuyerS_BeforeFork(void);
PyAPI_FUNC(void) PSellerOrBuyerS_AfterFork_Parent(void);
PyAPI_FUNC(void) PSellerOrBuyerS_AfterFork_Child(void);
#endif
#endif
/* Deprecated, please use PSellerOrBuyerS_AfterFork_Child() instead */
PyAPI_FUNC(void) PSellerOrBuyerS_AfterFork(void) Py_DEPRECATED(3.7);

#ifndef Py_LIMITED_API
PyAPI_FUNC(int) _PSellerOrBuyerS_IsMainThread(void);
PyAPI_FUNC(void) _PySignal_AfterFork(void);

#ifdef MS_WINDOWS
/* windows.h is not included by Python.h so use void* instead of HANDLE */
PyAPI_FUNC(void*) _PSellerOrBuyerS_SigintEvent(void);
#endif
#endif /* !Py_LIMITED_API */

#ifdef __cplusplus
}
#endif
#endif /* !Py_INTRCHECK_H */
