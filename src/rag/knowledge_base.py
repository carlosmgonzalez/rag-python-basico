KNOWLEDGE_BASE = [
    {
        "id": "doc_001",
        "text": "Para reiniciar el servidor Nginx en Ubuntu ejecuta: sudo systemctl restart nginx. Verifica el estado con: sudo systemctl status nginx.",
        "metadata": {"fuente": "manual_ops.pdf", "seccion": "Servidores", "pagina": 12},
    },
    {
        "id": "doc_002",
        "text": "Las variables de entorno se configuran en el archivo .env en la raíz del proyecto. Nunca subas el archivo .env a Git. Usa .env.example como plantilla.",
        "metadata": {"fuente": "guia_dev.pdf", "seccion": "Configuración", "pagina": 3},
    },
    {
        "id": "doc_003",
        "text": "El límite de rate en nuestra API es de 1000 requests por minuto por usuario. Si lo superas recibirás un error 429. Implementa exponential backoff en el cliente.",
        "metadata": {"fuente": "api_docs.pdf", "seccion": "Rate Limits", "pagina": 8},
    },
    {
        "id": "doc_004",
        "text": "Para hacer deploy a producción: 1) Corre los tests con pytest, 2) Build la imagen Docker, 3) Push al registry, 4) Aplica el helm chart con kubectl.",
        "metadata": {"fuente": "deploy_guide.pdf", "seccion": "DevOps", "pagina": 22},
    },
    {
        "id": "doc_005",
        "text": "La base de datos PostgreSQL corre en el puerto 5432. Las credenciales están en Vault bajo el path secret/prod/postgres. Nunca uses las credenciales de prod en local.",
        "metadata": {
            "fuente": "infra_docs.pdf",
            "seccion": "Base de Datos",
            "pagina": 5,
        },
    },
    {
        "id": "doc_006",
        "text": "Para restaurar un backup de la base de datos: pg_restore -U postgres -d mydb backup.dump. Los backups se generan automáticamente cada noche a las 2am UTC.",
        "metadata": {
            "fuente": "infra_docs.pdf",
            "seccion": "Base de Datos",
            "pagina": 7,
        },
    },
]

INVESTOR_DATA = """
Logan Finance Corporation Non-QM Purchasing and
Underwriting Guidelines [Open Road Update]
July 28 2025 - March 9, 2026
1.12 Prepayment Penalty [Loan amount threshold updated to meet PA state law]
Loans with prepayment penalties are not eligible for owner-occupied or second home
properties. A prepayment penalty is required for investment properties, and the
prepayment penalty should be equal to six months interest on the amount prepaid that
exceeds 20% of the original principal balance unless otherwise restricted by State law.
This is known as the California Rule prepay formula.
Alternatively, a fixed percentage of no less than 3% - The prepayment charge will be equal
to a fixed percentage and applied to any curtailment or the entire outstanding principal
balance during the prepay period.
A prepayment penalty of at least one year is required unless prohibited by state law.
In either case, the prepayment penalty applies to loans that pay off due to sale or
refinance (a “hard” prepay).
Logan has the following PPP restrictions case:
Prepayment Penalty not permitted in any of the following states:
 Properties located in Alaska, Kansas, and New Mexico
 Properties located in Illinois with individual vesting and a note rate above 7.99%
 Properties located in New Jersey not vested in a Corporation (C or S Corp) and a
note rate above 5.99%
 Properties located in Pennsylvania containing 1-2 units and a loan amount below $
329,411
 1 unit Properties located in Michigan
 1-2 unit properties located in Ohio
 Purchase loans located in Rhode Island
Limitations
 Properties located in Cook County Illinois with loan amounts less than $250,000
must meet IL PPP requirements and require a 3/2/1 step down PPP
 Properties located in Minnesota not permitted for conforming loan limits.
 Properties located in Mississippi step down pre-payment required
2.2.9.5 Ineligible Project Types [Require requirement to follow FNMA guidelines for
critical vs non critical repairs]
In addition to Fannie Mae’s Ineligible Projects, the following are not allowed: without
exception:
o Timeshares
o Condotels/ Condo Hotels
o Co-ops
o Mobile or Manufactured Home Condominium Projects
o House Boats
o Community Apartments, Tenant-in-Common aka “own-your-own” Projects, or
other multifamily property types with exclusive use to a specific apartment licensed
or leased to an interest owner or shareholder
o Units offered through filings with the United States Securities and Exchange
Commission
o Projects with Non-Conforming Use of Land where zoning prohibits rebuild in the
event of total or partial destruction
o Projects with revenue sharing agreements with 3rd parties managing the project for
short-term rental
o Projects in which year-round occupancy is prohibited
o The project is not located on contiguous parcels of land (buildings separated by
public and private streets, or amenities are okay)
o Multi-family units
o Assisted living units
o Units containing transfer fees
o Projects where the subject unit will be transient in nature
Following Characteristics are considered ineligible, however may be considered for exception review
and possible LLPA (characteristics cannot result in layered risk and must be supported with compensating factors for consideration).
o Units less than 500 square feet
o Units that are not held fee simple
o Condominium conversions with less than two years seasoning (not including gut
rehab’s)
o Projects with mandatory or upfront periodic membership fees
o Projects for which the HOA is subject to pending litigation for the safety, structural
soundness, or habitability of the project
 Projects where HOA’s engineer’s report demonstrates that the defects claimed
are neither safety, nor structural soundness related can be considered on an
exception basis
o Projects where safety and structural soundness repairs have been made and HOA is
suing for reimbursement of funds, and additional capital to cure remaining defects may
also be considered on an exception basis Projects with pending litigation not fully
covered by insurance
o Projects with outstanding critical repairs per Fannie Mae guidelines including but not
limited to items that present structural integrity, life-safety, or habitability risks, or
indicate significant deferred maintenance that may impair the long-term soundness of
the project
 Project that have noncritical repairs per Fannie Mae guidelines are eligible
without exception, which are include but are not limited to maintenance-related
or capital improvement items that do not pose immediate structural, safety, or
habitability concerns and are commonly planned, budgeted, or addressed
through reserve funding. Additional documentation will be required
o Projects with greater than 60% investor occupancy
 For Primary and Secondary Residence transactions, investor occupancy
requirement is waived
o Projects with single entity ownership of greater than 25% (other than the original
sponsor or developer)
o Project where the common areas and amenities are not fully completed
o Project where the subject phase is not 100% complete
o Projects with 49 units or less – and exceeds 35% commercial space
o Projects with 50 or more units – and exceeds 50% commercial space
o Projects with 20% or more of the units 60+ days delinquent to the homeowner’s
association, whether regular or special assessment
o Projects located in Florida and California where the insurance deductible is greater than
7-10% 5% will require project financials to ensure sufficient funds to cover deductible in
case of claim
o Projects with budgets for capital reserves less than 5% of total expenditures
 If HOA maintains in its reserve bank accounts more than 50% of the annual
operating expenditures, annual reserve requirement is waived
 If a project shows a reserve study, and demonstrates that it is following the
recommendations of the reserve study, 5% reserve requirement is satisfied
 For new construction projects, developer/sponsor capital contributions can be
used to meet the reserves requirement
2.2.9.7 Limited Condominium Review: (applicable to warrantable condominium only)
[Projects with non-critical repairs are permitted for limited review]
 Minimum Square Feet 500
 Unit held Fee Simple
 The project must be established, 75% of the units conveyed, construction complete, and
HOA control transferred to the unit owners
 The condominium HOA must not be involved in active or pending litigation that disqualifies
the property from a limited review, except for minor litigations as defined by Fannie Mae
 Projects with significant deferred maintenance failed milestone/building recertifications, or
other regulatory directives and code violations for repairs due to unsafe conditions are
ineligible
o Projects with ongoing critical repairs must demonstrate there are no safety and
structural soundness findings or related required repairs outstanding to be eligible
for Limited Review
o Projects with non-critical repairs as defined by Fannie Mae will follow Fannie Mae
requirements for condo review type
o Projects in the middle of Building Recertification/Milestone require Non-
warrantable Full Review, and Exception consideration. Structural and Safety related
repairs must be completed for consideration
 Commercial space in the project is limited to max 35% of project square footage
 The project must be 100% complete with no future phases to be built or annexed
 Projects cannot be managed as a hotel, motel, or be primarily transient in nature
 Projects may not have mandatory upfront or periodic membership fees for recreational
amenities owned or operated by a 3rd party or original developer
 Projects for senior care or life care facilities are ineligible
 Projects where a single entity owns more than the 25% not eligible for limited review
 No more than 15% of total units may be 60 days or more past due on common expense or
special assessments
 HOA must not receive more than 10% of its budgeted income from non-incidental business
operations
 Replacement reserves for capital expenditures and deferred maintenance must be at least
5% of the budget
o If the project holds in reserve accounts an amount equal to or greater than 50% of
the project’s annual operating expenses, 5% reserve requirement is satisfied
o If a project shows a reserve study, and demonstrates that it is following the
recommendations of the reserve study, 5% reserve requirement is satisfied
2.2.9.11 Condominium Documentation: [Additional documentation required for condos
with repairs]
 Condominium questionnaire
 Master Insurance Policy
 HOA budget and Balance Sheet dated within 90 days
 Title Report
 Declaration of condominium
 Bylaws
 Association rules and regulations
 Legal compliance certification
 Appraisal report
 Any project with non-critical repairs requires the following additional documentation
o Required documentation is limited to confirming awareness, funding, and
reasonable execution planning.
o Documentation of any special assessments related to the repairs
o HOA budget and/or financials demonstrating adequate funding
o Any available inspections, certifications, or recertifications
o Most recent reserve study, if available and applicable
 Any project with critical repairs requires the following additional documentation to consider
an exception
o Complete engineer’s report addressing the condition of the building
o Letter from a licensed engineer or contractor confirming:
o The building is structurally sound during the repair period
o No life-safety or habitability concerns exist while repairs are ongoing
o No impact on accessibility during or after repairs
o Signed HOA letter or most recent two HOA board meeting minutes confirming:
o Awareness of repairs
o Budget allocation
o Estimated completion plan
o Most recent reserve study (if available), dated within three (3) years
3.1.2 Title Exceptions [Guidelines to follow FNMA requirements for Oil and mineral
rights]
Logan will not purchase a mortgage secured by property that has an unacceptable title
impediment, particularly unpaid real estate taxes and survey exceptions. If survey is not
commonly required in particular jurisdictions, the Seller must provide on ALTA 9
Endorsement. If it is not customary in a particular area to supply either the survey or an
endorsement, the title policy must not have a survey exception.
The following title exceptions are permissible regarding loans sold to Logan, provided that
they are also permissible in accordance with Fannie Mae’s title insurance requirements:
 Customary public utility subsurface easements, the location of which are fixed and can
be verified.
 Above-surface public utility easements that extend along one or more property lines for
distribution purposes or along the rear property line for drainage, provided they do not
extend more than 12 feet from the subject property lines and do not interfere with any of
the buildings or improvements, or with the use of the subject property, and further
provided their violation will not result in the forfeiture or reversion of title or a lien of any
kind for damages, or have an adverse effect on the fair market value of the subject
property.
 Mutual easement agreements that establish joint driveways or party walls constructed
on the subject property and on an adjoining property, provided all future owners have
unlimited and unrestricted use of them.
 Encroachments on one foot or less on adjoining property by eaves or other overhanging
projections or by driveways provided there is at least a ten (10) foot clearance between
the buildings on the subject property and the property line affected by the
encroachments.
 Encroachments on the subject property by improvements on adjoining property
provided these encroachments extend one foot or less over the property line of the
subject property, have a total area of 50 square feet or less, do not touch any buildings,
and do not interfere with the use of any improvements on the subject property or the
use of the subject property not occupied by improvements.
 Encroachments on adjoining properties by hedges or removable fences.
 Liens for real estate or ad valor taxes and assessments not yet due and payable.
• Outstanding oil, water, or mineral rights as long as they do not materially alter the
contour of the property or impair its value or usefulness for its intended purposes.
5.3 Vesting and Ownership [Layered LLC’s permitted with the below
requirements]
Ownership must be fee simple title. Title must be in the Borrowers name at the time of
application for refinance transactions. Loans held in an LLC or Trust at the time of the
application for refinance transactions are permitted if the following are met:
 If the property was owned prior to closing by a limited liability corporation (LLC) that
is majority-owned or controlled by the Borrower(s)
 If the property was owned prior to closing by an inter vivos revocable trust the
Borrower must be the primary beneficiary of the trust.
Eligible forms of vesting are:
 Individuals
 Tenants in common
 Joint tenants
 Inter vivos revocable trust
Ineligible forms of vesting are:
 Land trusts
 IRAs
 Blind trusts
 LP’s
Title vesting in an inter vivos revocable trust is permitted when the requirements set forth
in this section are followed. The Fannie Mae requirements should be followed to the
extent this section is silent. Any created greater than or equal to 5 years of the application
date a trust certificate is required.
The trust must be established by one or more natural persons, solely or jointly. The
primary beneficiary of the trust must be the individual(s) establishing the trust. The trust
must become effective during the lifetime of the person establishing the trust. If the trust
is established jointly, there may be more than one primary beneficiary as long as the
income or assets of at least one of the individuals establishing the trust will be used to
qualify for the mortgage.
The trustee must include either:
 The individual establishing the trust (or at least one of the individuals, if two (2) or more.
 An institutional trustee that customarily performs trust functions and is authorized to
act as trustee under the laws of, the applicable state.
The trustee must have the power to hold the title, and mortgage the property. This must be
specified in the trust. One or more of the parties establishing the trust must use personal
income or assets to qualify for the mortgage. The following documentation is required:
 If the trust was created under California law, a fully executed Certificate of Trust under
Section 18100.5 of the California Probate Code.
 If the trust was created under the laws of a state other than California:
o Attorney's Opinion Letter from the Borrower's attorney or Certificate of Trust
verifying all the following:
 The trust is revocable.
 The Borrower is the settler of the trust and the beneficiary of the trust.
 The trust assets may be used as collateral for a loan.
 The trustee is:
 Duly qualified under applicable law to serve as trustee
 The Borrower
 The settler
 Fully authorized under the trust documents and applicable law
to pledge, or otherwise encumber the trust asset
In addition to the vesting’s listed above business purpose/investment loans will allow a
loan to close in an LLC or Corporation if all of the following requirements are met:
 The LLC or Corporation is formed in the United States.
 Each Member/Owner of the LLC or Corporation with 20% or greater ownership of the
LLC or Corporation must be a Guarantor for the loan and meet the credit qualifications
of these guidelines.
 The LLC or Corporation is owned by Individual(s).A Layered LLC is permitted if the
following are true
o Each Owning LLC is owned by Individual(s) members
o No more than 2 LLC’s own the vesting LLC
 A Corporation is not eligible if it is owned by another entity.
If the Guarantor is closing in an LLC, the following documentation is required for review:
 IRS EIN Letter, Bank Verified EIN, or State Verified EIN
 Certificate / Articles of Formation / Organization
 Operating Agreement inclusive of all schedules, amendments and resolutions.
Corporate resolutions/amendments changing ownership interest dated mid-
application are not permitted.
 Certificate of Good Standing or evidence of active status on states website
If the Guarantor is closing in a Corporation the following documentation is required:
 IRS EIN Letter, Bank Verified EIN, or State Verified EIN
 Articles of Incorporation
 Certificate of Incumbency and/or Corporate Bylaws setting forth Corporate Officer(s)
and Director(s)
 Current Stock Ledger
 Corporate Resolutions (if applicable). Corporate resolutions/amendments changing
ownership interest dated mid-application are not permitted.
 Certificate of Good Standing or evidence of active status on states website
In addition to the below documents must be completed as follow
 Loan Application
o Completed for each Personal Guarantor of the entity
o Signed by the Personal Guarantor ‘s of the entity
 Personal Guaranty
o Completed for each Personal Guarantor of the entity
o Signed by the PG and signed and dated the same date of the note
 Note
o Signed by the Personal Guarantor
 Mortgage w/Riders
o Signed by the PG
o Vested in Entity
 W-9
o In entity name including EIN
 Disclosures
o State or Federal disclosures signed by the Personal Guarantor
Example signature block below for the note, security instrument and all riders
ABC Investor, LLC a (______) limited liability company
_______John Guarantor____
By: John Guarantor
Title: [ Member, Managing Member etc..]
And
ABC Investor , LLC a (______) limited liability company
_______Joe Guarantor____
By: Joe Guarantor
Title: [ Member, Managing Member etc..]
6.6 Mortgage and Housing History Requirements [First time homebuyer and first time
investor broken out into separate sections]
6.6.1 First Time Home Buyer
First Time Home Buyer defined as an individual who has not had ownership of a property
either solely, jointly or through an entity within the preceding three year period.
6.6.2 First Time Investor
First time investor defined as an investor that does not have at least twelve (12) months of
experience owning and/or managing income-producing real estate within the most recent
thirty-six (36) months from the origination of the Note.
6.6.5 Mortgage and Housing History Requirements Open Road Elevated Full Doc, Open
Road Elevated Bank Statement, Open Road Elevated Asset Qualification, Open Road
Elevated DSCR [Requirements for Elevated Programs]
No Borrower may be more than 0x30x24 on any mortgage or rental payment for a property
located in the United States.
All borrowers must document their current housing payment history for the most recent 24
months. If the credit report does not reflect the current housing payment history, the
following documentation is required:
 Mortgage and/or HELOC payments:
o Loan payment history from the servicer or third-party verification service,
o Verification of mortgage (VOM) from an institutional lender OR most recent
24 months cancelled checks or bank statements
o Verification of mortgage (VOM) from a private lender OR 24 months
cancelled checks or bank statements.
 Rent payments:
o Canceled checks can be provided. In lieu of cancelled checks, the lender
may use the borrower’s bank statements, copies of money orders or other
reasonable methods for documenting timely housing payments. The
documentation must clearly indicate the payee and amount being paid
and reflect the payments were made on a consistent basis for the last 24
months; or
o Direct Verification of payment of rent from the landlord, both Individual
landlords and management companies for the 24 months
 Owned free and clear:
o Most recent 24 months property taxes paid on time
 First Time Home Buyer
o Not Permitted
 First Time Investor
o Not Permitted [Investment properties only]
6.6.6 Investor Experience Open Road Elevated Full Doc, Open Road Elevated Bank
Statement, Open Road Elevated Asset Qualification, Open Road Elevated DSCR
[Requirements for Elevated Programs]
Any Borrower applying for a business purpose loan under any of the following programs
must have experience managing an investment property for the most recent 24 months as
of the Note Date.
 Open Road Elevated Full Doc,
 Open Road Elevated Bank Statement,
 Open Road Elevated Asset Qualification,
 Open Road Elevated DSCR
6.9 Derogatory Credit [Requirements added for Elevated]
The seasoning requirement for derogatory credit is four years for Bankruptcy, Foreclosure,
Short Sale/Deed in lieu for Open Road Full Doc, Open Road Bank Statements, Open Road
Profit and Loss, Asset Qualification, Open Road No Ratio , Open Road Condotel, Open
Road, Elevated Full Doc, Open Road Elevated Bank Statement, Open Road Elevated Asset
Qualification, Open Road Elevated DSCR loans
The seasoning requirement for derogatory credit is three years for Bankruptcy,
Foreclosure, Short Sale/Deed in lieu for Open Road Debt Service Coverage Ratio Loans
The length of time will be measured based on the below:
 Bankruptcy: by the discharge/dismissal date to the Note date.
 Foreclosure: by the settlement date to the Note date, unless included in a bankruptcy
then the discharge date of the bankruptcy to the Note date will be used.
 Short Sale/Deed-in-lieu: by the completion date to the Note date unless included in a
bankruptcy then the discharge date of the bankruptcy to the Note date will be used.
7.4.1  Forbearance, loan modifications, or deferrals are treated as a short sale / deed-in-lieu
for eligibility and pricing purposes.
Open Road Full Documentation Program and Open Road Elevated Full Documentation
[Addition of new program]
7.4.1.2.1 Self-Employment – Open Road Elevated Full Doc and Open Road Elevated Asset
Qualification [New Requirement for Elevated programs]
In addition to the requirements in Section 7.4.1.2, a 5-year history of being self-employed in
the same business is required for Open Road Elevated Full Doc. This is only required for
Open Road Elevated Asset Qualification if self employed income is being used to qualify.
7.4.2 Open Road Bank Statement Program and Open Road Elevated Bank Statement
Program [Addition of new program]
7.4.2.1 Required History of Self-Employment [Additional requirement for Open Road Elevated
Bank Statement]
In order to be eligible for the Open Road Bank Statement Program at least one Borrower
must be self-employed for at a minimum of two years prior to the Note date.
In order to be eligible for the Open Road Elevated Bank Statement Program at least one
Borrower must be self-employed in the same business for at a minimum of five years prior
to the Note date.
In order to be considered self-employed for the Borrower must be at a minimum 25% owner
in the business the income is derived from.
Self-employment length and ownership percentage must be documented by one of the
following ways:
 Letter from a 3rd party tax professional
 Business license
 LLC or Partnership agreements
 Incorporation records
Verify the existence of the business within 120 days of the Note date and ensure the
business is active, with the following:
 a letter from either the businesses tax professional, regulatory agency or licensing
bureau, certifying two (2) years of self‐employment in the same business, or
 either a phone listing and/or business address using directory assistance or an
internet search.
7.4.4 Open Road Asset Qualification Program and Open Road Elevated Asset
Qualification program [Addition of new Elevated program]
The Open Road Asset Qualification Program uses a 60-month depletion rate or if the borrower
is qualified using the 60-month depletion rate in addition to the reserves listed on the matrix,
the borrower must additionally have 110% of the original principal balance in reserve.
The Open Road Elevated Asset Qualification Program uses a 120-month depletion rate or if the
borrower is qualified using the 120-month depletion rate in addition to the reserves listed on
the matrix, the borrower must additionally have 110% of the original principal balance in
reserve.
7.4.4.2.2 Open Road Elevated Asset Qualification Income Calculation [Income
requirement for new Asset Qualification program]
Borrowers qualifying using 120-month Asset Qualification calculation, the Borrower’s
documented reserves are at least 110% of the original principal balance of the Loan plus
applicable reserves per the program matrix and the Borrowers’ Income from Asset
Qualification plus the Borrowers’ Income from Other Sources are sufficient so the
Borrowers’ debt to income ratio does not exceed 43%.
Monthly Borrowers’ Income from Asset Qualification is determined by using total
documented reserves divided by 120.
7.4.5 Open Road Debt Service Coverage Ratio and Open Road Elevated Debt Service
Coverage Ratio [Addition of Elevated Debt Service Coverage Program]
8.8 IPCs [90% option added]
Interested Party Contributions (IPC’s) that exceed the limits below are considered sales
concessions.
Occupancy Type LTV/CLTV Ratio Maximum IPC
Principal residence or 2nd home
75.01%-90% 6%
75% or less 9%
Investment All LTV/CLTV's 3%
9.8 Open Road Elevated Full Doc [New Program]
Primary Residence
Purchase- Full Doc – Primary
Credit Score $5,000,000
740+ 65%
Rate Term - Full Doc – Primary
Credit Score $5,000,000
740+ 65%
Cash Out - Full Doc – Primary
Credit Score $5,000,000
740+ 65%
2nd Home
Purchase- Full Doc – 2nd Home
Credit Score $5,000,000
740+ 65%
Rate Term - Full Doc – 2nd Home
Credit Score $5,000,000
740+ 65%
Cash Out - Full Doc – 2nd Home
Credit Score $5,000,000
740+ 65%
Investor/Business Purpose
Purchase- Full Doc – Investor
Credit Score $4,500,000
740+ 65%
Rate Term - Full Doc – Investor
Credit Score $4,500,000
740+ 60%
Cash Out - Full Doc – Investor
Credit Score $4,500,000
740+ 60%
Reserves
18 Months
Cash Out Used as Reserves Allowable, Must have 18 Months reserves made up of their own funds
Additional Restrictions
Interest Only Only 30 Year Term Permitted
First Time Home Buyer Not Permitted
Non-Occupant Co
Borrower Primary Residence Only, Cash out Not Permitted
2-4 Unit Not Permitted on Primary and 2nd Homes. 2 Units permitted on Investment
Non-Warrantable Condo Permitted – No structural repairs
Florida Condos Purchase Only
Rural Properties Max 15 Acres, Primary and 2nd Home Only no cash out
Declining Markets 5% Reduction to LTV
Cash in hand No Restriction
Minimum Loan Amount Primary and 2nd Home $3,000,001/ $2,000,001 Investor Business purpose
Housing History 0x30x24
Credit Event Seasoning 4+ Years
Max Financed Properties 20
Max Borrowers/Guarantors 4
Max DTI 43%
Gift of Equity Not Permitted
Self Employed 5+ Years Required
Investor Experience 2+ Years [Investor/Business Purpose Only]
9.9 Open Road Elevated Bank Statements [New Program]
Primary Residence
Purchase- Bank Statement – Primary
Credit Score $5,000,000
740+ 65%
Rate Term - Bank Statement – Primary
Credit Score $5,000,000
740+ 65%
Cash Out - Bank Statement – Primary
Credit Score $5,000,000
740+ 65%
2nd Home
Purchase- Bank Statement – 2nd Home
Credit Score $5,000,000
740+ 65%
Rate Term - Bank Statement – 2nd Home
Credit Score $5,000,000
740+ 65%
Cash Out - Bank Statement – 2nd Home
Credit Score $5,000,000
740+ 65%
Investor/Business Purpose
Purchase- Bank Statement – Investor
Credit Score $4,500,000
740+ 65%
Rate Term - Bank Statement – Investor
Credit Score $4,500,000
740+ 60%
Cash Out - Bank Statement – Investor
Credit Score $4,500,000
740+ 60%
Reserves
18 Months
Cash Out Used as Reserves Allowable Must have 18 Months reserves made up of their own funds
Additional Restrictions
Interest Only Only 30 Year Term Permitted
First Time Home Buyer Not Permitted
Non-Occupant Co
Borrower Primary Residence Only, Cash out Not Permitted
2-4 Unit Not Permitted on Primary and 2nd Homes. 2 Units permitted on Investment
Non-Warrantable Condo Permitted No structural repairs
Florida Condos Purchase Only
Rural Properties Max 15 Acers, Primary and 2nd Home Only, no cash out
Declining Markets 5% Reduction to LTV
Cash in hand No Restriction
Minimum Loan Amount Primary and 2nd Home $3,000,001/ $2,000,001 Investor Business purpose
Housing History 0x30x24
Credit Event Seasoning 4+ Years
Max Financed Properties 20
Max Borrowers/Guarantors 4
Max DTI 43%
Gift of Equity Not Permitted
Self Employed 5+ Years Required
Investor Experience 2+ Years [Investor/Business Purpose Only]
9.10 Open Road Elevated Asset Qualification [New Program]
Primary Residence
Purchase- Asset Depletion – Primary
Credit Score $5,000,000
740+ 65%
Rate Term - Asset Depletion – Primary
Credit Score $5,000,000
740+ 65%
Cash Out - Asset Depletion – Primary
Credit Score $5,000,000
740+ 65%
2nd Home
Purchase- Asset Depletion – 2nd Home
Credit Score $5,000,000
740+ 65%
Rate Term - Asset Depletion – 2nd Home
Credit Score $5,000,000
740+ 65%
Cash Out - Asset Depletion – 2nd Home
Credit Score $5,000,000
740+ 65%
Investor/Business Purpose
Purchase- Asset Depletion – Investor
Credit Score $4,500,000
740+ 65%
Rate Term - Asset Depletion – Investor
Credit Score $4,500,000
740+ 60%
Cash Out - Asset Depletion – Investor
Credit Score $4,500,000
740+ 60%
Reserves
110% of the Loan amount + 18 Months
Cash Out Used as Reserves Not Allowed
Additional Restrictions
Interest Only Only 30 Year Term Permitted
First Time Home Buyer Not Permitted
Non-Occupant Co
Borrower Primary Residence Only, Cash out Not Permitted
2-4 Unit Not Permitted on Primary and 2nd Homes. 2 Units permitted on Investment
Non-Warrantable Condo Permitted No structural repairs
Florida Condos Purchase Only
Rural Properties Max 15 Acers, Primary and 2nd Home Only, no cash out
Declining Markets 5% Reduction to LTV
Cash in hand No restriction
Minimum Loan Amount Primary and 2nd Home $3,000,001/ $2,000,001 Investor Business purpose
Housing History 0x30x24
Credit Event Seasoning 4+ Years
Max Financed Properties 20
Max Borrowers/Guarantors 4
Max DTI 43%
Asset Depletion (mos) 120
Gift of Equity Not Permitted
Self Employed 5+ Years Required
Investor Experience 2+ Years [Investor/Business Purpose Only]
9.11 Open Road Elevated DSCR [ New Program]
Investor/Business Purpose
Purchase- DSCR – Investor/Business Purpose
Credit Score $4,500,000
740+ 65%
Rate Term - DSCR – Investor/Business Purpose
Credit Score $4,500,000
740+ 60%
Cash Out - DSCR – Investor/Business Purpose
Credit Score $4,500,000
740+ 60%
Reserves
18 Months
Cash Out Used as Reserves Allowable, Must have 18 Months reserves made up of there own funds
Additional Restrictions
Interest Only 30 Year term only
First Time Home Buyer Not Permitted
First Time Investor Not Permitted
2-4 Unit Max 2 Units
Warrantable Condo Permitted
Non Warrantable Condo Permitted No structural repairs
Florida Condo Purchase Only
Rural Properties Not permitted
Declining Markets 5% Reduction to LTV
Vacant Properties Purchase only
Max Financed Properties 20
Max Borrowers/Guarantors 4
Cash in hand No Restriction
Minimum Loan Amount $2,000,001
Short Term Rental Not permitted
Housing History 0x30x24
Credit Event Seasoning 4+ Years
Min DSCR 1.25
Non Arm’s Length Not Permitted
Gift of Equity Not Permitted
Investor Experience 2+ Year
"""
