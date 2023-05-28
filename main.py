import openai

def split_string(long_string, max_length=2048):
    return [long_string[i:i + max_length] for i in range(0, len(long_string), max_length)]

# Set the string that will contain the summary
long_string = """STANDARD FORM OF APARTMENT LEASE
(FOR APARTMENTS NOT SUBJECT TO THE RENT STABILIZATION LAW)
THE REAL ESTATE BOARD OF NEW YORK. INC
Copyright 2019. All Rights Reserved. Reproduction in whole or in part prohibited.
REBNY Apt non-stab 2019 Rev 7.19
PREAMBLE: This lease contains the agreements between Tenant and Owner concerning the rights and
obligations of each party. Tenant and Owner have other rights and obligations which are set forth in government
laws and regulations.
Tenant should read this Lease carefully. If Tenant has any questions, or if Tenant does not understand any
words or statements herein, obtain clarification from an attorney. Once Tenant and Owner sign this Lease,
Tenant and Owner will be presumed to have read it and understood it completely. Tenant and Owner admit that
all agreements between Tenant and Owner have been written into this Lease. Tenant understands that any
agreements made before or after this Lease was signed and not written into it will not be enforceable.
April
05
2023
THIS LEASE is made as of
between
month
day
year
NEW YORK. NY 10107
and Tenant (hereinafter referred to "Tenant' or "Lessee*) RAID AHMED, MICHAEL ZIEGLER
whose address is
Please note the following paragraphs that require a selection among alternative wording: 2, 3E, 34
Please note the following paragraphs that require deletions If inapplicable: 9D, 12C(), 12E, 25, 32C/0), 33, 34, 35, 36, 37, 38, 59, 60
Please note the following paragraphs that require the insertion of terms (and/or delete if inapplicable): 1, 2, 3A, 3B, 4, 9D, 12B, 12C,
25, 32C, 34A, 35, 38B, Exhibit A (Memorandum Confirming Term), Exhibit C (Owner's Work), Exhibit D (Apartment Furniture)
APARTMENT AND USE
Owner agrees to lease to Tenant Apartment,
(the "Apartment") on the
floor
in
the
building at 34 ST MARKS PLACE, NEW YORK, NY 10003
(the "Building"),
Borough of NEW YORK
City and State of New York. Tenant shall use the Apartment for living purposes only and for
no other purpose (such restricted purposes includes, but are not limited to, any commercial activity or illegal or dangerous activity).
The Apartment may only be occupied by Tenant and the following Permitted Occupants (and occupants as permitted in accordance
with Real Property Law $235-f:
Tenant acknowledges that no other person other than Tenant and the Permitted Occupants may reside in the Apartment without
the prior written consent of the Owner. If Tenant violates any of the terms of this provision, the Owner shall have the right to restrain the
same by injunctive relief and/or any other remedies provided for under this Lease and at law and/or equity.
LEASE COMMENCEMENT DATE: LENGTH OF LEASE
representative. The "Lease Commencement Date" is
Tatival case Eftectiv: Diatende the dati. & luly4 791282 ) ease is retwred to Mar ant pro Tenants ogpressentative Ryasemer, Periti
(that 'neans'Ine hangin), of chit'tense Went Dealin in the Dias. commencemenp" astmax b whir@vided.for g6)/ 30/2024nis Lease, the terro
*Term*). Tenant acknowledges that notwithstanding anything to the contrary contained in this Lease: () the Term of this Lease may be
reduced provided for herein and (ii) the Term shall consist of the period beginning with the Lease Commencement Date through and
jActuding, the date that is the last day of the month in which the [CHOOSE ONE AND CROSS OUT THE OTHER ALTERNATIVES] (one
(1) year)|two (2) year|(Two
(2) month(g)] anniversary of the Lease Commencement Date occurs.
3.
RENT
A. 'Rent is defined as the base rent due under this Lease. Tenant's monthly Rent for the Apartment is $ 3,750.00
per month.
Tenant must pay Owner the Rent, in equal monthly installments, on the first day of each month either to Owner at the above address or
at another place that Owner may inform Tenant of by written notice.
B. When Tenant signs this Lease, Tenant must pay by bank or cashier's check (or by electronic fund transfer, if instructed by
Owner as described below), the following:
(1) one (1) months' Rent (i.e., $ 3,750.00,.
(i) the Security Deposit (in the amount stated in Article 4): and
(ili) any commission due by Tenant to the Brokers (as defined in Article 34 hereinafter) in connection with this
Lease.
C. If the Lease Commencement Date shall not occur on the first day of a calendar month, the Rent for such calendar month shall
be prorated on a per diem basis. If the Lease begins after the first day of the month, Tenant must pay when it signs this Lease one (1)
full months' Rent and for the next full calendar month Tenant shall pay a prorated Rent based on the number of days the Lease began
after the first day of the month (for example, if the beginning date of this Lease is the 167 day of the month, Tenant would pay for fifteen
(15) out of thirty (30) days, or one-half (1/2), of a full months' Rent for the second calendar month). In any event, if the Lease
Commencement Date shall not occur on the first day of a calendar month, the Term shall also include the remainder of the month in which
the Lease Commencement Date occurred.
D. Within five (5) business days after the request of Owner, at Owner's option, Tenant shall return a document supplied by Owner
in the form attached hereto as Exhibit A (a "Memorandum Confirming Term*) confirming the Lease Commencement Date, the Rent
Commencement Date (if different than the Lease Commencement Date) the Lease expiration date and any other material terms of this
Lease, certifying that Tenant has accepted delivery of the Apartment and that the condition of the Apartment complies with Owner's
obligations hereunder. Tenant's failure to so deliver the Memorandum Confirming Term shall be considered a material default under this
Lease, however, Tenant's failure to do so shall not affect the occurrence of the Lease Commencement Date or the validity of this Lease
or alter the terms and provisions contained in the Memorandum Confirming Term if so delivered to Tenant by Owner.
E. Tenant may be required to pay other charges to Owner under the terms of this Lease, such additional charges shall be referred
to as "Additional Rent*. Any Additional Rent must be paid by Tenant to Owner upon the earlier of () the first day of the month immediately
following the month said Additional Rent is billed to Tenant or () fifteen (15) days from the date Tenant is billed for the Additional Rent
If Tenant fails to pay the Additional Rent on time, Owner shall have the same rights against Tenant as if Tenant failed to pay Rent. Said
Rent and Additional Rent must be paid in full in accordance with the foregoing, without deduction or offset and without the need for
demand or notice from Owner. Except as may be provided for otherwise in this Article 3, all Rent and Additional Rent shall be payable to Owner by (check], (direct deposit] [CROSS OUT ANY FORM OF PAYMENT THAT IS INAPPLICABLE) or such other form of payment
as required by Owner only. If by direct deposit, Owner shall provide Tenant the necessary wiring instructions.
F. Tenant shall be entitled to a five (5) day grace period for the payment of any sum of Rent or Additional Rent due under this
Lease. Any sum of Rent or Additional Rent not paid within five (5) days of the date due shall be subject to a late fee of the lesser of (i)
$50.00, or (i) five percent (5%) of the unpaid amount. Interest shall also be payable on the aforesaid late Rent or Additional Rent beginning
thirty (30) days from the due date, such interest accruing at the lesser of (1) the maximum amount allowable by law, or (ii) one and one-
half percent per month (1.5%), until the late Rent or Additional Rent is paid in full. There shall be a Fifty Dollar ($50.00) fee for any check
which is dishonored or returned. Any late charge or interest charge shall be considered Additional Rent.
G. Owner need not give notice to Tenant to pay Rent. Rent must be paid in full and no amount subtracted from it. The whole
amount of Rent is due and payable as of the Lease Commencement Date. Payment of Rent in installments is for Tenant's convenience
only. If Tenant is in default under any of the terms and conditions of this Lease, Owner may give notice to Tenant that it may no longer
pay Rent in installments and the entire Rent for the remaining part of the Term will then immediately be due and payable.
SECURITY DEPOSIT
Tenant is required to give Owner the sum of $ 3,750.00
(such amount not to exceed one (1) months' Rent pursuant to
This Security Deposit shall not bear interest, unless if otherwise required by applicable law. In the eveot that the Security Deposit shall
earn interest, then in such event Owner shall be entitled to an administrative fee pursuant to applicable law
If Tenant carries out all of Tenant's agreements in this Lease and if Tenant moves out of the Apartment and returns it to Owner
vacant, broom clean and in the same condition it was in when Tenant first occupied it, except for ordinary wear and tear or damage
caused by fire or other casualty through no fault of Tenant, Owner will return to Tenant the full amount of the Security Deposit within
fourteen (14) days after the later of () the date this Lease ends, or (I) the date Tenant vacates the Apartment. However, if Tenant is in
default of Tenant's obligations under this Lease and/or there are any damages to the Apartment beyond ordinary wear and tear or damage
caused by fire or other casualty, Owner may keep all or part of the Security Deposit to cover reasonable repairs of such damage and
Owner shall provide Tenant with an itemized statement indicating the basis for the amount of the Security Deposit retained within the
aforementioned fourteen (14) day period. Furthermore, for sake of clarity and emphasis, (.) if Tenant does not carry out all of Tenant's
obligations under this Lease, Owner may keep all or part of the Security Deposit necessary to pay Owner for any losses incurred, including
missed payments and (i) Owner's retention of the Security Deposit as allowable under this Lease shall not be deemed to be Owner's
sole remedy for any default by Tenant of Tenant's obligations pursuant to the terms and conditions of this Lease.
TENANT ACKNOWLEDGES AND AGREES THAT THE SECURITY DEPOSIT CANNOT BE USED TOWARDS RENT OR
ADDITIONAL RENT BY TENANT. Notwithstanding anything to the contrary contained in this Lease, if Owner shall apply all or any portion
of the Security Deposit to cure a default by Tenant hereunder during the Term of this Lease, Tenant shall, within five (5) business days
deposit with Owner that sum which shall be necessary to maintain the security in an amount equal to the Security Deposit as so required
in this Article 4. Failure to replenish the Security Deposit in a timely manner shall be deemed a default under this Lease.
If Owner sells the Apartment, Owner, at its sole option, will turn over Tenant's security either to Tenant or to the person buying
the Apartment within five (5) days after the sale. Owner will then notify Tenant, by registered, certified or overnight mail by a nationally
recognized overnight courier, of the name and address of the person or company to whom the deposit has been turned over. In such
case, Owner will have no further responsibility to Tenant for the Security Deposit and the new owner will become responsible to Tenant
for the Security Deposit.
IF TENANT IS UNABLE TO MOVE IN
Except as otherwise provided herein, Owner shall not be liable for failure to give Tenant possession of the Apartment on the
Lease Commencement Date. Rent shall be payable as of the beginning of this Lease Term unless Owner is unable to give Tenant
possession. A situation could arise which might prevent Owner from letting Tenant move into the Apartment on the Lease Commencement
Date. If this happens for reasons beyond Owner's reasonable control, Owner will not be responsible for Tenant's damages or expenses,
and this Lease will remain in effect. However, in such case, this Lease will start on the date when possession is available, and the ending
date of this Lease as specified in Article 2 will remain the same (unless otherwise mutually agreed to in writing by Tenant and Owner).
Tenant will not have to pay Rent until the date possession is available, or the date Tenant moves in, whichever is earlier (however, in no
event shall Tenant move in or take possession prior to the date Owner shall have given Tenant notice that Tenant may take possession
of the Apartment). Owner will notify Tenant as to the date possession is available. If Owner does not give Tenant notice that possession
is available within thirty (30) days after the Lease Commencement Date, provided that Owner's failure to deliver possession is not due to
a Tenant delay, Tenant may send a fifteen (15) day written termination notice (the "Termination Notice") to Owner, and if Owner is unable
to deliver possession within fifteen (15) days of receipt of Tenant's Termination Notice, this Lease shall terminate and be of no further
force and effect and all prepaid Rent, the Security Deposit and any other fees paid by Tenant (except for non-refundable fees required in
the Lease package) at the execution of this Lease shall be promptly returned to Tenant.
6.
CAPTIONS
7.
In any dispute arising under this Lease, in the event of a conflict between the text and a caption, the text controls.
WARRANTY OF HABITABILITY
A. All of the sections of this Lease are subject to the provisions of the Warranty of Habitability Law. Under that law, Owner
agrees that the Apartment is fit for human habitation and that there will be no conditions which will be detrimental to life, health or safety.
B. Tenant will do nothing to interfere with or make more difficult Owner's efforts to provide Tenant and all other occupants
of the Building with the required facilities and services. Any condition caused by Tenant's misconduct or the misconduct of Tenant
Parties (as hereinafter defined) or anyone else under Tenant's direction or control shall not be a breach by Owner.
8.
CARE OF TENANT'S APARTMENT: END OF LEASE: MOVING OUT
A. At all times during the Term of this Lease, Tenant will take good care of the Apartment and will not permit or do any damage
to it, except for damage which occurs through ordinary wear and tear. Tenant shall, at Tenant's own cost and expense, make all repairs
caused or occasioned by Tenant or Tenant's agents, contractors, invitees, licensees, guests or servants (collectively hereinafter "Tenant
Parties"). In addition, Tenant shall promptly notify Owner and/or the Building Superintendent/Building Manager in writing upon the
occurrence of any problem, malfunction or damage to the Apartment Tenant will move out on or before the ending date of this Lease and
leave the Apartment in good order and in the same condition as it was when Tenant first occupied it, except for ordinary wear and tear
and damage caused by fire or other casualty through no fault of Tenant.
B. CLEANING. Tenant is required to use only non-abrasive cleaning agents in the Apartment. Tenant is responsible for damage
done by use of any improper cleaning agents.
C. If Tenant fails to maintain the Apartment or make a needed repair or replacement as required hereunder, Owner may hire a
professional and make such maintenance, repairs or replacements at Tenant's sole cost and expense. Owner's reasonable expense will
be payable by Tenant to Owner as Additional Rent within ten (10) business days after Tenant receives a bill from Owner.
D. When this Lease ends, Tenant must remove all of Tenant's movable property. Tenant must also remove at Tenant's own
expense, any wall covering, bookcases, cabinets, mirrors, painted murals or any other installation or attachment Tenant may have
installed in the Apartment, even if it was done with Owner's consent. Tenant must restore and repair to its original condition those portions
of the Apartment affected by those installations and removals. Tenant has not moved out until all persons, furniture and other property of
Tenant's is also out of the Apartment. If Tenant's property remains in the Apartment after this Lease ends, Owner may either treat Tenant as still in occupancy and charge Tenant for use, or may consider that Tenant has given up the Apartment and any property remaining in
the Apartment. In this event, Owner may either discard the property or store it at Tenant's expense. Tenant agrees to pay Owner for all
costs and expenses incurred in removing such property. The provisions of this article will continue to be in effect after the end of this
Lease.
E.
Except as provided for otherwise in Article 35 of this Lease, in the event that (i) Owner intends to offer to renew this Lease with
a Rent increase equal to or greater than five (5%) percent above the then current Rent, or (I) Owner does not intend to renew this Lease,
Owner shall provide Tenant written notice as follows:
If Tenant has occupied the Apartment for less than one (1) year and does not have a Lease Term of at least one
(1) year, Owner shall provide at least thirty (30) days' notice;
If Tenant has occupied the Apartment for more than one (1) year but less than two (2) years, or has a Lease Term
of at least one (1) year but less than two (2) years, Owner shall provide at least sixty (60) days' notice; or
If Tenant has occupied the Apartment for more than two (2) years or has a Lease Term of at least two (2) years,
Owner shall provide at least ninety (90) days' notice.
F. Within a reasonable time after notification of either party's intention to terminate this Lease, unless Tenant provides less than
two (2) weeks' notice of Tenant's intention to terminate, Owner shall notify Tenant in writing of Tenant's right to request an inspection
before vacating the Apartment. Tenant shall have the right to be present at said inspection. Subject to the foregoing, if Ten ant requests
such inspection, the inspection shall be made no earlier than two (2) weeks and no later than one (1) week before the end of the tenancy
Owner shall provide at least forty-eight (48) hours written notice of the date and time of the inspection. After the inspection, Owner shall
provide Tenant with an itemized statement specifying repairs, cleaning or other deficiencies that are proposed to be the basis of any
deductions from the Security Deposit. If Tenant requests such inspection, Tenant shall be given an opportunity to remedy any identified
deficiencies prior to the end of the tenancy (or, at Owner's sole option, if Tenant fails to remedy any such identified deficiencies, Owner
may remedy such identified deficiencies at Tenant's sole cost and expense as described hereinafter). Any and all repairs or alterations
made to the Apartment as a result of said inspection shall be at Tenant's sole cost and expense. Said repairs must be approved by Owner
and shall be performed, at Owner's sole option by (1) licensed and adequately insured Tenant's contractors in a good and skillful manner
with materials of quality and appearance comparable to existing materials and approved by Owner or (ii) by Owner's contractor(s).
CHANGES AND ALTERATIONS TO APARTMENT
A. Tenant cannot build in, add to, change or alter, the Apartment in any way, including, but not limited to, installing, changing, or
altering any paneling, wallpaper, flooring. "built in" decorations, partitions, railings, paint, carpeting, plumbing, ventilating, air conditioning,
electric, or heating systems without first obtaining the prior written consent of Owner which may be withheld in Owner's sole discretion. If
Owner's consent is given, the alterations and installations shall become the property of Owner when completed and paid for by Tenant.
They shall remain with and as part of the Apartment at the end of the Term. Notwithstanding the foregoing, Owner has the right to demand
that Tenant remove the alterations and installations at the end of the Lease Term, and in such case Tenant shall repair all damage
resulting from said removal and restore the Apartment to its original condition, including any holes in the wall or damage caused by the
removal of any pictures, artwork or TV mounts hung by Tenant on the walls. Any and all work shall be performed by Tenant in accordance
with the terms and conditions of this Lease and in accordance with all applicable laws, rules, regulations and codes of any governmental
or quasi-governmental entity. Tenant's contractor shall also supply, before performing any such work, a certificate of insurance naming
Owner and the Building's managing agent (if applicable) as additional insured.
B. Without Owner's prior written consent, Tenant cannot install or use in the Apartment any of the following: dishwasher machines,
clothes washing or drying machines, electric stoves, garbage disposal units, heating, ventilating or air conditioning units or any other
electrical equipment which, in Owner's reasonable opinion, will overload the existing wiring installation in the Building or interfere with the
use of such electrical wiring facilities by other tenants of the Building. Also, Tenant cannot place in the Apartment water-filled furniture.
C. If a lien is filed on the Apartment or Building due to Tenant's fault, Tenant must promptly pay or bond the amount stated in the
lien. Owner may pay or bond the Lien if Tenant fails to do so within ten (10) days after Tenant has written notice about the lien, in which
case, Owner's costs shall be paid by Tenant as Additional Rent.
D. APPROVED ALTERATIONS. [DELETE IF INAPPLICABLE] Anything contained herein to the contrary notwithstanding,
provided that both Owner and Tenant have acknowledged their agreement te the follewing by each party affixing their initiels immediatety
betow this provision, Owner hereby consents to the following alterations to be performed by Tenant, at Tenant's sote cost and expense,
but for the sake of clarity and emphasis all other terms and conditions of this tease including, without limitation, the terms and conditions
contained
this
Article
hereof)
shalt
stilt
apply-
Owner Initiat:
-Fenant Initial:
10.
TENANT'S DUTY TO OBEY AND COMPLY WITH LAWS, REGULATIONS AND RULES
A. GOVERNMENT LAWS AND ORDERS. Tenant will obey and comply (I) with all present and future city, state and federal
laws rules, regulations and codes of any governmental or quasi-governmental entity or body which affect the Building or the Apartment,
and (ii) with all orders and regulations of insurance rating organizations which affect the Apartment and the Building. Tenant will not
allow any windows in the Apartment to be cleaned from the outside unless the prior written consent of the Owner is obtained.
8. OWNER'S RULES AFFECTING TENANT. Tenant, its Permitted Occupants and Tenant Parties must obey all Owner's rules
(the "Owner's Rules and Regulations") annexed hereto and made apart hereof as Exhibit B and all future reasonable rules of Owner
or Owner's agent. Notice of all additional rules shall be delivered to Tenant in writing or posted in the lobby or other public place in the
building. Owner shall not be responsible to Tenant for not enforcing any rules, regulations or provisions of another tenant's lease
except to the extent required by law.
C.
. TENANT'S RESPONSIBILITY. Tenant is responsible for the behavior of Tenant, the Permitted Occupants of the Apartment,
the Tenant Parties and any other people who are visiting the Apartment. Tenant will reimburse Owner as Additional Rent upon demand
for the cost of all losses, damages, fines and reasonable legal expenses incurred by Owner because Tenant, the Permitted Occupants
of the Apartment, the Tenant Parties or any other people visiting the Apartment have not obeyed applicable laws, rules, regulations
and codes of any governmental or quasi-governmental entity or rules of this Lease.
OBJECTIONABLE CONDUCT
Tenant, the Permitted Occupants of the Apartment, the Tenant Parties or any other people visiting the Apartment will not engage
in objectionable conduct at the Apartment or the Building. Objectionable conduct (*Objectionable Conduct) means behavior which makes
or will make the Apartment or the Building less fit to live in for Tenant or other occupants. It also means anything which interferes with the
right of others to properly and peacefully enjoy their apartment, or causes conditions that are dangerous, hazardous, unsanitary or
detrimental to other occupants of the Building. Objectionable Conduct by Tenant, the Tenant Parties, or any other people visiting the
Apartment, gives Owner the right to end this Lease on six (6) days' written notice to Tenant that this Lease will end.
12.
SERVICES AND FACILITIES
A. REQUIRED SERVICES. Owner will provide (1) cold and hot water and heat as required by law, (il) repairs to the Apartment
not caused by Tenant ( subject to the terms and conditions of this Lease), the Tenant Parties or any other people visiting the Apartment,
as required by law, (ili) elevator service if the Building has elevator equipment; and (iv) the utilities, if any, included in the Rent, as set
forth in subparagraph B below. Tenant is not entitled to any Rent reduction because of a stoppage or reduction of any of the above
services unless it is provided by law. 8.
The following utilities are included in the Rent. NONE
INSERT "NONE" IF NO UTILITIES ARE INCLUDED IN THE RENTI
C.
ELECTRICITY AND OTHER UTILITIES. Tenant acknowledges and understands that Owner has no obligation to supply, or
liability in connection with, utilities or services in or to the Apartment (except as may be provided for otherwise in this Lease). Tenant
shall be responsible, at Tenant's sole cost and expense, for securing, air conditioning, electricity, gas, cable, phone, and all other
utilities and services (except as may be provided for otherwise in this Lease).
0
Tenant shall contract directly with the appropriate utility provider for all aforementioned services (not including the
utilities included in the Rent as provided for in subparagraph B).
f) Notwithstanding anything to the contrary contained in this tease, the Owner provides the following services
for a seperate, sub-metered charge. It is covenanted and agreed by Tenant-
that alt the aforesaid costs and expenses shall be paid by Tenant to Owner within five (5) days afterrendition of any
bill or statement to Tenant theretor DELETE 14 INAPPLICABLE.
D.
Stopping or reducing of service(s) will not be reason for Tenant to stop paying Rent, to make a money claim or to claim
constructive eviction. Damage to the equipment or appliances supplied by Owner, caused by Tenant's acts, omissions or neglect, or
the act, omission or neglect of the Tenant Parties or any other person visiting the Apartment, shall be repaired at Tenant's sole cost
and expense. In the event that Tenant fails to make such repairs within a reasonable period of time, Owner shall have the option to
make such repairs at Tenant's expense and charge the same to Tenant as Additional Rent. Damage to the equipment or appliances
supplied by the Owner, which are not caused by Tenant's negligence, acts or misuse or the negligence, acts or misuse of the Tenant
Parties or any other people visiting the Apartment, shall be promptly repaired by the Owner at the Owner's sole cost and expense
Owner may stop service of the plumbing, heating, elevator, air cooling or electrical systems, because of accident, emergency, repairs,
or changes until the work is complete. Notwithstanding the foregoing, except in emergency situations, Owner shall provide Tenant no
less than twenty-four (24) hours prior written notice of any planned service stoppages. Owner shall take all necessary steps to ensure
that service stoppages do not interfere with Tenant's use and enjoyment of the Apartment.
E.
APPLIANCES. Appliances supplied by Owner in the Apartment are for Tenant's use. They shall be in working order on the
date hereof and will be maintained and repaired or replaced by Owner, except If repairs or replacement are made necessary because
of Tenant's or the Tenant Parties' negligence or misuse, Tenant will pay Owner for the cost of such repair or replacement as Additional
Rent. Notwithstanding anything te the contrary centained in this Lease, provided the appliance in need of repair has been delivered in
working order on the Lease Commencement Date, Tenant shall be responsible for the initial $
in cost of such appliance's-
repair or replacement-[DELETE IF INAPPLICABLE OR INSERT AMOUNT]. Tenant must not use a dishwasher, washing machine,
dryer, freezer, heater, ventilator or other appliance unless installed by Owner or with Owners prior written consent (in its sole
discretion). Tenant must not use more electric than the wiring or feeders to the Building can safely carry.
F. FACILITIES AND AMENITIES. If Owner permits Tenant to use any storeroom, storage bin, laundry or any other facility
located in the Building but outside of the Apartment (e.g., fitness center, resident lounge, roof deck, golf simulator, movie theater
swimming pool, spa, etc.), the use of any such facility will be furnished to Tenant free of charge and at Tenant's own risk. Tenant will
operate at Tenant's expense any coin operated appliances located in any such facility. Owner shall have no obligation to provide any
of the aforementioned facilities or any type of doorman, attendant, porter or any other type of similar service at the Building, and Owner
may discontinue same without being liable to Tenant therefor or without in any way affecting this Lease or the liability of Tenant
hereunder or causing a diminution of Rent and the same shall not be deemed to be lessening or a diminution of facilities or services
within the meaning of any law, rule or regulation now or hereafter enacted, promulgated or issued.
13.
INABILITY TO PROVIDE SERVICES
Because of a strike, labor trouble, national emergency, repairs, or any other cause beyond Owner's reasonable control, Owner
may not be able to provide or may be delayed in providing any services or in making any repairs to the Building. In any of these events,
any rights Tenant may have against Owner are only those rights which are allowed by laws in effect when the reduction in service occurs
14.
ENTRY TO APARTMENT
During reasonable hours and with reasonable notice, except in emergencies, Owner and Owner's representatives, agents
and employees may enter the Apartment for the following reasons:
To erect, use and maintain pipes and conduits in and through the walls and ceilings of the Apartment; inspect; exterminate;
install or work on master antennas or other systems or equipment; and to perform other work and make any and all repairs, alterations,
or changes Owner decides are necessary. Tenant Rent will not be reduced because of any of the foregoing.
B. To show the Apartment to potential buyers or lenders.
C. For ninety (90) days before the end of the Lease Term, to show the Apartment to persons who wish to lease it.
D. If, during the last month of the Lease, Tenant has moved out and removed all or almost all of Tenant's property from the
Apartment, Owner may enter the Apartment to make changes, repairs, or redecorations. Tenant's Rent will not be reduced for that
month and this Lease will not be ended by Owner's entry.
E. If, at any time, Tenant is not personally present to permit Owner or Owner's representatives, agents or employees to enter
the Apartment and entry is necessary or allowed by law or under this Lease, Owner or Owner's representatives, agents or employees
may nevertheless enter the Apartment. Owner may enter by force in an emergency. Owner or Owner's representatives, agents or
employees will not be responsible to Tenant, unless during such entry, any authorized party is negligent or misuses Tenant's property.
15.
ASSIGNING; SUBLETTING; ABANDONMENT
A. ASSIGNING AND SUBLETTING. Tenant cannot assign this Lease or sublet all or part of the Apartment or permit any other
person to use the Apartment (other than a Permitted Occupant without the prior written consent of the Owner, which Tenant
acknowledges may be withheld by Owner in its sole and absolute discretion, for any reason or no reason. If Tenant assigns this Lease
or sublet all or part of the Apartment and fail to obtain Owner's prior written consent, in addition to any and all other rights of Owner
under this Lease and at law and/or in equity, Owner has the right to cancel the Lease. Tenant must get Owner's written permission as
provided for herein, each time Tenant wants to assign or sublet. Permission to assign or sublet is good only for that assignment or
sublease. Tenant remains bound to the terms of this Lease after an assignment or sublet is permitted, even if Owner accepts money
from the assignee or subtenant. The amount accepted will be credited toward money due from Tenant, as Owner shall determine. The
assignee or subtenant does not become Owner's tenant. Tenant is responsible for acts and neglect of any person in the Apartment.
Notwithstanding the foregoing, Owner expressly reserves the right to terminate this Lease with respect to the Apartment upon the
receipt by Owner of any request for assignment or sublease (*Owner's Recapture Right*). Owner's Recapture Right, if exercised, must
be sent to Tenant in writing within thirty (30) days after Tenant's request to assign or sublet the Apartment. In the event that Owner
consents to an assignment and elects not to exercise Owner's Recapture Right, Tenant shall reimburse Owner for all of Owner's
attorneys' fees in connection with the review of the assignment or sublease. In the event that Owner agrees to an assignment or
sublease, subject to applicable law, Owner shall be entitled to one hundred percent (100%) of any consideration or rent over and
above that Rent provided for in this Lease. The sublease shall provide that the subtenant shall, at Owner's option, attorn to Owner
upon any termination of this Lease.
B.
ABANDONMENT. If Tenant moves out of the Apartment (abandonment) before the end of this Lease without the consent
of Owner, this Lease will not be ended. Tenant will remain responsible for each monthly payment of Rent and Additional Rent as it
becomes due until the end of this Lease. In case of abandonment, Tenant's responsibility for Rent and Additional Rent will end only if
Owner chooses to end this Lease for default as provided in Article 16. 16.
DEFAULT
A. Tenant defaults under the Lease if Tenant acts in any of the following ways:
0
Tenant fails to carry out any agreement or provision of this Lease;
() Tenant does not take possession or move into the Apartment fifteen (15) days after the beginning of this Lease;
or
(*) Tenant and the Permitted Occupants of the Apartment move out permanently before this Lease ends:
if Tenant defaults in any one of these ways, other than a default in the agreement to pay Rent and/or Additional Rent, Owner
may serve Tenant with a written notice to stop or correct the specified default within ten (10) days. Tenant must then either stop or
correct the default within such ten (10) day period, or, if the nature of the default is not reasonably capable of being cured within such
ten (10) day period, then Tenant must begin to take all steps necessary to correct the default within ten (10) days and thereafter
diligently continue to do all that is necessary to correct the default as soon as possible (however, in no event shall any extension of
the aforesaid ten (10) day period exceed thirty (30) days).
B. If Tenant does not stop, correct or begin to materially correct a default within ten (10) days as provided for above, or engages
in Objectionable Conduct, Owner shall give Tenant a written notice that this Lease will end six (6) days after the date such written
notice is sent to Tenant. At the end of the six (6) day period, this Lease will end and Tenant then must move out of the Apartment.
Even though this Lease ends, Tenant will remain liable to Owner for unpaid Rent and/or Additional Rent up to the end of this Lease,
and damages caused to Owner after that time as stated in Article 17.
C. If Owner does not receive the Rent and/or Additional Rent within five (5) days of when this Lease requires, Owner or
Owner's agent shall send Tenant, via certified mail, a written notice stating the failure to receive such Rent and/or Additional Rent.
Provided Owner has served Tenant with a fourteen (14) day written demand, and Owner does not receive the overdue Rent (and
Additional Rent, as applicable) within fourteen (14) days after such written fourteen (14) demand for Rent (and Additional Rent, as
applicable) has been made, Owner may commence an action or summary proceeding seeking the payment of all Rent and/or Additional
Rent. If the Lease ends, Owner may do the following: (I) enter the Apartment and retake possession of it if Tenant has moved out or
(i) go to court and ask that Tenant and all other occupants in the Apartment be compelled to move out.
Once this Lease has been ended, whether because of default or otherwise, Tenant gives up any right Tenant might otherwise
have to reinstate this Lease
17
REMEDIES OF OWNER AND TENANT'S LIABILITY
If this Lease is ended by Owner because of Tenant's default, the following are the rights and obligations of Tenant and Owner.
- Tenant must pay Rent and Additional Rent until this Lease has ended. Thereafter, Tenant must pay an equal amount for
what the law calls "use and occupancy" until Tenant actually moves out.
B. Once Tenant is out, Owner may re- rent the Apartment or any portion of it for a period of time which may end before
or after the ending date of this Lease. Owner may re-rent to a new tenant at a lesser rent or may charge a higher rent than the Rent
in this Lease. Notwithstanding the foregoing, if Tenant vacates the Apartment in violation of the terms of this Lease, only then shall
Owner use reasonable efforts to re-rent the Apartment at the lesser of the fair market value of the Apartment or the Rent paid
hereunder.
C. Whether the Apartment is re-rented or not, Tenant must pay to Owner as damages:
0
the difference between the Rent in this Lease and the amount, if any, of the rents collected in any later lease of
the Apartment for what would have been the remaining period of this Lease; and
(©) Owner's expenses for the cost of getting Tenant out and re-renting the Apartment, including, but not limited to,
putting the Apartment in good condition, repairing damages, decorating and/or cleaning the Apartment for re-rental,
advertising the Apartment and for real estate brokerage fees; and
(.) Owner's expenses for attorney's fees (except in the event of a default judgment).
D. Tenant shall pay all aforementioned damages due in monthly installments on the Rent day established in this Lease. Any
legal action brought to collect one or more monthly installments of damages shall not prejudice in any way Owner's right to collect the
damages for a later month by a similar action.
E. If the Rent collected by Owner from a subsequent tenant of the Apartment is more than the unpaid Rent and damages
which Tenant owes Owner, Tenant cannot receive the difference. Owner's failure to re-rent to another tenant will not release or change
Tenant's liability for damages. Except as may be provided for otherwise in Article 17(B) of this Lease, Owner is not required to re-rent
the Apartment.
18.
ADDITIONAL OWNER REMEDIES; LEGAL FEES
If Tenant does not do everything Tenant has agreed to do, or if Tenant does anything which shows that Tenant intends not to do
what Tenant has agreed to do, Owner has the right to ask a Court to make Tenant carry out Tenant's agreements or to give the Owner
such other relief as the Court can provide. This is in addition to the remedies in Article 16 and 17 of this Lease.
19.
FEES AND EXPENSES (INCLUDING BUT NOT LIMITED TO LEGAL FEES)
Tenant must reimburse Owner for any of the following fees and expenses incurred by Owner:
0)
Making any repairs to the Apartment or the Building, including any appliances in the Apartment, which result from
misuse, omissions or negligence by Tenant, the Permitted Occupants of the Apartment, the Tenant Parties or
any other visitors to the Apartment;
(O
Correcting any violations of city, state or federal laws or orders and regulations of insurance rating organization
concerning the Apartment or the Building which Tenant, the Permitted Occupants of the Apartment, the Tenant
Parties, or any other persons who visit the Apartment or work for Tenant have caused;
(.) Preparing the Apartment for the next tenant if Tenant moves out of the Apartment before the Lease ending date
without Owner's prior written consent;
(N) Any legal fees and disbursements for the preparation and service of legal notices; legal actions or proceedings
brought by Owner against Tenant because of a default by Tenant under this Lease; or for defending lawsuits
brought against Owner because of the actions of Tenant, the Permitted Occupants of the Apartment, the Tenant
Parties or any other persons who visit the Apartment;
(v) Removing any of Tenant's property from the Apartment after this Lease is ended;
(vi) Any miscellaneous charges payable to the Owner for services Tenant requested that are not required to be
furnished Tenant under this Lease for which Tenant has failed to pay the Owner and which Owner has paid;
(vi) All other fees and expenses incurred by Owner because of the failure to obey any other provisions and
agreements of this Lease by Tenant, the Permitted Occupants of the Apartment, the Tenant Parties or any other
persons who visit the Apartment or work for Tenant.
These fees and expenses shall be paid by Tenant to Owner as Additional Rent within ten (10) business days after Tenant receives
Owner's bill or statement. if this Lease has ended when these fees and expenses are incurred, Tenant will still be liable to Owner for the
same amount as damages. In the event Tenant does not reimburse Owner within such ten (10) business day period, Owner shall be
entitled to deduct the fees and expenses from the Security Deposit. B. Tenant has the right to collect reasonable legal fees and expenses incurred in a successful defense by Tenant of a lawsuit
brought by Owner against Tenant or brought by Tenant against Owner to the extent provided by Real Property Law, Section 234.
20.
PROPERTY LOSS, DAMAGES OR INCONVENIENCE
Tenant understands and agrees that unless caused by the gross negligence or willful misconduct of Owner or Owner's
representatives, agents or employees, none of these authorized parties are responsible to Tenant for any of the following () any loss of
or damage to Tenant or Tenant's property in the Apartment or the Building due to any accidental or intentional cause, including a theft
or another crime committed in the Apartment or elsewhere in the Building: (li) any loss of or damage to Tenant's property delivered to any
employee of the Building (e.g., doorman, superintendent, etc.); or (ili) any damage or inconvenience caused to Tenant by actions
negligence or violations of their lease made by any other tenant or person in the Building except to the extent required by law. Tenant
further understands and agrees that Owner's employees are not authorized by Owner to care for Tenant's personal property. Owner is
not responsible for any loss, theft, damage to Tenant's personal property, or any injury caused by the property or its use by Building
employees.
Owner will not be liable for any temporary interference with light, ventilation, or view caused by construction by or on behalf of
Owner. Owner will not be liable for any such interference on a permanent basis caused by construction on any parcel of land not owned
by Owner. Owner will not be liable to Tenant for such interference caused by the permanent closing, darkening or blocking up of windows.
if such action is required by law. None of the foregoing events will cause a suspension or reduction of the Rent or allow Tenant to cancel
the Lease.
FIRE OR CASUALTY
A.
Tenant shall give Owner immediate notice in case of fire or other damage to the Apartment. If the Apartment becomes
unusable, in part or totally, because of fire, accident or other casualty, this Lease will continue unless ended by Owner under
subparagraph C below or by Tenant under subparagraph D below. However, the Rent will be reduced as of the date of the fire, accident
or other casualty. This reduction will be based upon the square footage of the Apartment which is unusable, as determined by Owner.
B. Owner will repair and restore the Apartment, unless Owner decides to take actions described in subparagraph C below. For
the sake of clarity and emphasis, Owner is not required to repair or restore the Apartment or replace the furnishings, decorations or
any of Tenant's property, and furthermore (unless otherwise agreed to by Owner in writing), Owner shall not be responsible for any
delays due to settling insurance claims, obtaining cost estimates, labor, material, equipment and/or supply problems, force majeure or
for any other delay beyond Owner's reasonable control. If the Lease is cancelled, Owner need not restore the Apartment.
C.
After a fire, accident or other casualty in the Building, Owner may decide to tear down the Building or to substantially rebuild
it. In such case, Owner need not restore the Apartment but may end this Lease. Owner may do this even if the Apartment has not
been damaged, by giving Tenant written notice of this decision within the later of sixty (60) days after the date when the damage
occurred or ten (10) business days after Owner is advised by its insurance carrier as to the amount of insurance proceeds it will have
available to restore the Apartment. If there is substantial damage to the Apartment or if the Apartment is completely unusable, Owner
may cancel this Lease by giving Tenant written notice of this decision within 30 days after the date when the damage occurred. If the
Apartment is unusable when Owner gives Tenant such notice, this Lease will end sixty (60) days from the last day of the calendar
month in which Tenant was given notice.
D. If the Apartment is completely unusable because of fire, accident or other casualty and it is not repaired in thirty (30) days,
Tenant may give Owner written notice that Tenant ends the Lease. If Tenant gives that notice, this Lease is considered ended on the
day that the fire, accident or casualty occurred. Owner will promptly refund Tenant's Security Deposit and the pro-rata portion of Rent
(and Additional Rent, as applicable) paid for the month in which the casualty happened.
E. Unless prohibited by the applicable policies, to the extent that such insurance is collected, Tenant and Owner release and
waive all right of recovery against the other or anyone claiming through or under each by way of subrogation.
F. Tenant acknowledges that if fire, accident, or other casualty causes damage to any of Tenant's personal property in the
Apartment, including, but not limited to Tenant's furniture and clothes, the Owner will not be responsible to Tenant for the repair or
replacement of any such damaged personal property unless such damage was as a result of the Owner's negligence.
22.
PUBLIC TAKING
The entire Building or a part of it can be acquired (condemned) by any government or government agency for a public or quasi-
public use or purpose. If this happens, this Lease shall end on the date the government or agency take title. Tenant shall have no claim
against Owner for any damage resulting; Tenant also agrees that by signing this Lease, Tenant assigns to Owner any claim against the
government or government agency for the value of the unexpired portion of this Lease.
23.
SUBORDINATION CERTIFICATES AND ACKNOWLEDGMENTS
Notwithstanding any provisions to the contrary contained in this Lease, this Lease and Tenant's rights, are subject and subordinate
to all present and future: (a) leases for the Building or the land on which it stands, (b) Owner's mortgage(s) now existing or hereinafter
existing), (c) agreements securing money paid or to be paid by a lender, and (d) terms, conditions, renewals, changes of any kind and
extensions of the mortgages, leases or lender agreements. If certain provisions of any such mortgage come into effect, the holder of any
such mortgage can end this Lease and such parties may commence legal action to evict Tenant from the Apartment. If this happens,
Tenant acknowledges that Tenant has no claim against Owner or such lease or mortgage holder. If Owner requests, Tenant will sign
promptly any acknowledgment(s) of the "subordination" in the form that Owner may require. Tenant authorizes Owner to sign such
acknowledgments) for Tenant if Tenant fails to do so within five (5) days of Owner's request.
Tenant also agrees to sign (if accurate) a written acknowledgment within ten (10) days of request to any third party designated
by Owner that this Lease is in effect, that Owner is performing Owner's obligations under this Lease and that Tenant has no present
claim against Owner.
24.
TENANT'S RIGHT TO LIVE IN AND USE THE APARTMENT
If Tenant pays the Rent and any required Additional Rent on time and Tenant does everything Tenant has agreed to do in this
Lease, Tenant's tenancy cannot be cut off before the ending date, except as provided for otherwise in this Lease, including, but not limited
to, in Articles 21. 22, and 23.
25.
BILLS AND NOTICE; ELECTRONIC SIGNATURES
Any notice, statement, demand or other communication required or permitted to be given rendered or made by either party to the
other, pursuant to this Lease or pursuant to any applicable law or requirement of public authority, shall be in writing (whether or not so
stated elsewhere in this Lease) and shall be given by registered or certified mail, return receipt requested, or by overnight mail by a
nationally recognized overnight carrier (or via email] [DELETE IF INAPPLICABLE), addressed to each of the following parties:

Notwithstanding anything to the contrary contained in this Lease, any notice from Owner or Owner's agent or attorney may be
delivered to Tenant personally at the Apartment. Notices shall be deemed received the next business day if by overnight carrier, the date
of delivery if by personal delivery, or three (3) business days after being mailed if by registered or certified mail.
26.
GIVING UP RIGHT TO TRIAL BY JURY AND COUNTERCLAIM
Both Tenant and Owner agree to give up the right to a trial by jury in a court action, proceeding or counterclaim (excluding
compulsory counterclaims) on any matters concerning this Lease, the relationship of Tenant and Owner as lessee and lessor or
Tenant's use or occupancy of the Apartment. This agreement to give up the right to a jury trial does not include claims for personal
injury or property damage.
If Owner begins any court action or proceeding against Tenant which asks that Tenant be compelled to move out, Tenant
cannot make a counterclaim unless Tenant is claiming that Owner has not done what Owner is supposed to do about the condition ol
the Apartment or the Building.
27.
NO WAIVER OF LEASE PROVISIONS
A
Even if Owner accepts Tenant's Rent and/or Additional Rent or fails once or more often to take action against Tenant when
it has not done what Tenant has agreed to do in this Lease, the failure of Owner to take action or Owner's acceptance of Rent and/or
Additional Rent does not prevent Owner from taking action at a later date if Tenant does not do what Tenant has agreed to do herein.
B. Only a written agreement between Tenant and Owner can waive any violation of this Lease.
If Tenant pays and Owner accepts an amount less than all the Rent and/or Additional Rent due, the amount received shall
be considered to be in payment of all or part of the earliest Rent and/or Additional Rent due. It will not be considered an agreement by
Owner to accept this lesser amount in full satisfaction of all of the Rent and/or Additional Rent due unless there is a written agreement
between Tenant and Owner.
D. Any agreement to end this Lease and also to end the rights and obligations of Tenant and Owner must be in writing, signed
by Tenant and Owner or Owner's agent. Even if Tenant gives keys to the Apartment and they are accepted by Owner or Owner's
representative, this Lease is not ended.
28.
CONDITION OF THE APARTMENT; APARTMENT RENTED "AS IS"
By signing this Lease Tenant acknowledges that Owner, Owner's representatives or superintendent has not made any
representations or promises with respect to the Building or the Apartment except as herein expressly set forth.
After signing this Lease
but before Tenant begins occupancy, Tenant shall have the opportunity to inspect the Apartment with Owner or Owner's agent to determine the
condition of the Apartment. If Tenant requests such inspection, the parties shall execute a written agreement before Tenant begins occupancy of
the Apartment attesting to the condition of the Apartment and specifically noting any existing defects or damages. Before taking occupancy of
the Apartment, Tenant has inspected the Apartment (or Tenant has waived such inspection) and Tenant accepts it in its present
condition "as is." except for any condition which Tenant could not reasonably have seen during Tenant's inspection. Tenant agrees that
Owner has not promised to do any work in the Apartment except as specified in Exhibit C annexed hereto (if any) and made apart
hereof.
29.
HOLDOVER
A. At the end of the Term, Tenant shall: (i) return the Apartment to the Owner in broom clean, vacant and in good condition,
ordinary wear and tear excepted: (il) remove all of Tenant's property and all of Tenant's installations, alterations and decorations (if so
directed by Owner); and (iv) repair all damages to the Apartment and Building caused by moving; and restore the Apartment to its
condition at the beginning of the Term ordinary wear and tear excepted.
Tenant hereby indemnifies and agrees to defend and hold Owner harmless from and against any loss, cost, liability, claim,
damage, fine, penalty and expense (including reasonable attorneys' fees and disbursements but excluding consequential or punitive
damages) resulting from delay by Tenant in surrendering the Apartment upon the termination of this Lease, including any claims made
by any succeeding tenant or prospective tenant or successor landlord founded upon such delay.
If Tenant holds over possession after the expiration date of the Lease or earlier termination of the Lease term or any
extended term of this Lease, such holding over shall not be deemed to extend the term of this Lease or renew this Lease. Under no
circumstances () will such holdover constitute a month-to-month tenancy, (il) shall this Article 29 imply any right of Tenant to remain
in the Apartment after the expiration or earlier termination of this Lease, (ili) will Owner be prohibited from exercising any rights
permitted by law against a holdover tenant; or (iv) will any monies paid by Tenant or accepted by Owner (e.g., Rent, Additional Rent,
holdover rent or otherwise) after the expiration or earlier termination of this Lease be deemed to reinstate any form of tenancy between
Tenant and Owner. In connection with such holdover, Tenant shall pay the following charges for the use and occupancy of the
Apartment for each calendar month or part thereof (even if such part shall be a small fraction of a calendar month), which total sum
Tenant agrees to pay to Owner per month promptly upon demand, in full, without set-off or deduction:
TWO (2) times the highest monthly Rent set forth in this Lease, plus
Hems of Additional Rent that would have been payable monthly pursuant to this Lease, had this Lease not expired or
terminated,
The aforesaid provisions of this Article 29 shall survive the expiration or earlier termination of this Lease
30.
DEFINITIONS
Owner: The term "Owner" means the person or organization receiving or entitled to receive Rent and Additional Rent from
Tenant for the Apartment at any particular time other than a rent collector or managing agent of Owner. Owner is the person or
organization that owns legal title to the Apartment. It does not include a former owner, even if the former owner signed this Lease.
Tenant: The Term "Tenant" means the person or persons signing this Lease as lessee and the respective heirs, distributes,
executors, administrators, successors and assigns of the signer. This Lease has established a lessor-lessee relationship between

Owner and Tenant.
31.
SUCCESSOR INTERESTS
The agreements in this Lease shall be binding on Owner and Tenant and on those who succeed to the interest of Owner or
Tenant by law, by approved assignment or by transfer.
32.
INSURANCE
A As a material inducement for Owner to enter into this Lease, Tenant shall obtain (i) liability insurance insuring Tenant, the
Permitted Occupants of the Apartment, the Tenant Parties and any other people visiting the Apartment, and (ii) personal property
insurance insuring Tenant's furniture and furnishings and other items of personal property located in the Apartment. Tenant may not
maintain any insurance with respect to any furniture or furnishings belonging to Owner that are located in the Apartment unless
otherwise directed by Owner. Tenant acknowledges that Owner may not be required to maintain any insurance with respect to the
Apartment.
B.
Owner is not liable for loss, expense, or damage to any person or property, unless due to Owner's gross negligence or
wrongful acts. Owner is not liable to Tenant for permitting or refusing entry of anyone into the Building. Tenant must pay for damages
with an attorney reasonably acceptable to Owner. Tenant is responsible for all acts, omissions or neglect of the Tenant Parties.
Tenant shall indemnify and save harmless Owner from and against any and all liability, penalties, losses, damages,
expenses, suits and judgments arising from injury during the term of this Lease to person or property of any nature and also from any
matter growing out of the occupation of the Apartment, provided however that such is not the result of Owner's gross negligence or
wrongful acts or that of Owner's employees, or agents. Tenant agrees, at Tenant's sole cost and expense to procure and maintain at
all times during the Lease term the following insurance:
1) General tiability Insurance for an amount not less that
poticy of no tess than
Dottars ($.
AMOUNTS}, and
Dollars t$
> with an umbrella-
†ADELETE IF INAPPLICABLE OR INSERT
(.) Renters Insurance, which covers any, and all personal property or belongings contained in the Apartment. Tenant agrees
to hold Owner harmless regarding these personal belongings due to loss or damage except in cases of Owner's gross
negligence.
D.
The aforementioned insurance policies shall name Owner and the property manager (if applicable) as additional insureds
or interests, as applicable. In the event of Tenant's failure to procure and/or maintain the aforementioned policies prior to the date
possession of the Apartment is ready to be delivered to Tenant on the Lease Commencement Date, Owner may (i) refuse to deliver
possession of the Apartment to Tenant until such time as evidence of such insurance is delivered by Tenant to Owner (however,
Tenant shall nonetheless remain responsible for the payment of Rent and Additional Rent as of the Lease Commencement Date),
and/or (li) order such insurance policies, pay the premiums, and add the amount thereof to the Rent next coming due as Additional
Rent, and the Owner shall have all rights and remedies for the collection thereof as is provided for collection of ordinary Rent. The
abovementioned insurance policies shall provide for no less than thirty (30) days' notice of cancellation or modification to Owner, and
Tenant shall provide Owner with a copy of such insurance policies. Evidence of the aforesaid coverage being in place shall be
presented to the Owner on or before the first day of the term of this Lease and may be requested at any time during term of this Lease.
Such insurance policies are to be written by a good and solvent company licensed to do business in the state of New York. Tenant
shall immediately reimburse Owner for the cost of any insurance policy Owner obtains for the Apartment, including but not limited to
insurance for Owner's furniture or furnishings in the Apartment. Tenant acknowledges that Owner may not be required to maintain any
insurance with respect to the Apartment.
33.
FURNITURE [DELETE IF INAPPLICABLE)
The Apartment is being teased as fully furnished. All furniture and furnishings contained in the Apartment (the "Apartment-
Fumiture*) are listed in Exhibit O annexed hereto (if any) and made apart hereof. Tenant shall accept the Apartment Furniture "as is" on
the commencement date of this tease. Owner represents that all Apartment Furniture is in good repair and in working order on the
commencement date of this tease except as may be noted n Exhibit©.
Tenant shall take good care of the Apartment Furniture during the pendency of this Lease and shall be liable for any damages
caused by Tenant or Tenant Parties to the Apartment Furniture. Tenant shall not be responsible for any damages to the Apartment
Furniture not caused by Tenant or Tenant Parties or caused by ordinary wear and tear. Tenant shall surrender the Apartment Furniture
when this Lease terminates in the same condition as on the date this Lease commenced, subject to ordinary wear and tear. If a ny repairs
are required to the Apartment Furniture when this Lease terminates, Tenant shall pay Owner upon demand the cost of any required
repairs.
Tenant may not remove the Apartment Furniture from the Apartment or change the location of the Apartment Furniture during the
pendency of this Lease without Owner's prior written consent.
34.
BROKER (DELETE EITHER SUBPARAGRAPH A OR B; IF SUBPARAGRAPH B IS DELETED, INSERT NAME OF BROKER(S)
IN SUBPARAGRAPH A]
Owner and Tenant represent that in the negotiation of this Lease they dealt with no broker(s) other than
(the "Tenant's Broker) and
(the "Owner's Broker")
(hereinafter collectively referred to as the 'Broker*). Such Broker(s) will be compensated by [Tenant)(Owner) [CHOOSE ONE AND
CROSS OUT THE OTHER ALTERNATIVE) in accordance with a separate agreement subject to a fully executed and delivered lease.
B.
Tenant represents to Owner that Tenant has not dealt with any real estate broker in connection with the leasing of the
Apartment
C. Owner and Tenant hereby agree to indemnity, defend and hold harmless each other from and against any and all claims,
demands, liabilities, suits, losses, costs and expenses (including reasonable attorneys' fees and disbursements) arising out of any
35.
TENANT'S OPTION TO RENEW DELETE IF INAPPLICABLE: IF APPLICABLE, PLEASE INSERT NECESSARY
INFORMATION)
A
Tenant shall have the right to extend the term of this tease for
- Yeers) commeneng.
and ending on -
"the "Extension Term*) provided: (4) Tenant gives-Owner notice (the "Extension

during the Extension Term.
36.
TERRACES, BALCONIES AND BACKYARDS [DELETE IF INAPPLICABLE
All of the terms and conditions of this Lease apply to the terrace, balcony and/or backyard (as applicable). Tenant's use of the
terrace or balcony must comply with any rules that may be provided to Tenant by Owner
Tenant shall clean the terrace or balcony and keep the terrace or balcony free from snow, ice, garbage and other debris. No
cooking is allowed on the terrace or balcony except as may be otherwise permitted by law. Tenant may not install a fence or any addition
on the terrace or balcony. Tenant is responsible for making all repairs to the terrace or balcony if caused by Tenant, the Tenant Parties
or any other visitor to the Apartment, at Tenant's sole expense.
37.
LEAD PAINT DISCLOSURE (DELETE IF THE BUILDING WAS ERECTED AFTER 1978
Simultaneously with the execution of this Lease, Tenant and Owner shall sign and complete the disclosure of information on lead-
based paint and/or lead-based paint hazards annexed as a rider attached to this Lease. Tenant acknowledges receipt of the pamphlet,
"Protect Your Family From Lead in Your Home* prepared by the United States Environmental Protection Administration.
38.
PETS [DELETE EITHER SUBPARAGRAPH A OR B; IF SUBPARAGRAPH A IS DELETED, INSERT NECESSARY
INFORMATION IN SUBPARAGRAPH BI
Tenant may not keep any pets in the Apartment. IF TENANT BREACHES THIS SECTION, TENANT WILL FORFEIT
TWENTY PERCENT (20%] OF THE SECURITY DEPOSIT TO OWNER, TO COMPENSATE OWNER FOR ANY AND ALL COSTS
RELATING THERETO AS LIQUIDATED DAMAGES (AND NOT AS A PENALTY). TENANT ACKNOWLEDGES AND AGREES THAT
THE FOREGOING IS A MATERIAL INDUCEMENT FOR OWNER TO ENTER INTO THIS LEASE, AND BUT FOR SAID COVENANT,
OWNER WOUtD NOT HAVE EXECUTED THIS tEASE AGREEMENT.
Tenant may keep pets in the Apartment provided: () Tenant obtains the prior written consent of Owner, and (li) Tenant
complies with any rules with respect to the keeping of pets in the Apartment. Owner hereby consents to the following pet(s):
39.
KEYS/SECURITY
A. Tenant shall not remove, alter, or change in any way the existing locks, security codes or keys that are provided for the
Apartment or any part thereof. Tenant assumes liability for any person keys are entrusted to. The name, address and telephone
number of any person with an additional set of keys to the Apartment are required to be furnished to Owner or its managing agent.
Only Owner may make such additional sets of keys upon Tenant's written request with the abovementioned information. Owner will
not refuse any such reasonable request. All extra sets of keys must be returned to Owner no later than one (1) day prior to move out
unless agreed to by Owner. In the event that all keys are not returned to the Owner by or before the last day of tenancy, Tenant agrees
to pay for the replacement cost as mentioned below (or part thereof if Owner deems it appropriate).
B.
Tenant agrees and understands that Tenant will be charged a re-keying fee in the sum of $350.00 for the entrance door
each and every time a key replacement is required or deemed necessary by Owner if the need arises due to Tenant's loss of the key,
employee changes, or request. Said charges shall be deemed Additional Rent.
40.
WINDOW GUARDS
Simultaneously with the execution of this Lease, Tenant shall complete and deliver to Owner a notice with respect to the
installation of window guards in the Apartment in the form required by the City of New York annexed as a rider attached to this Lease.
Tenant acknowledges that it is a violation of law to refuse, interfere with installation, or remove window guards where required.
BED BUG DISCLOSURE
Tenant and Owner shall sign and complete the disclosure of bedbug infestation history annexed as a rider attached to this Lease
42.
SPRINKLER DISCLOSURE
Tenant and Owner shall sign and complete the sprinkler disclosure annexed as a rider attached to this Lease
43.
OCCUPANCY NOTICE FOR INDOOR ALLERGEN HAZARDS
Owner shall complete and deliver to Tenant the Occupancy Notice for Indoor Allergen Hazards annexed as a rider attached to this
Lease. Owner acknowledges that it has delivered to Tenant "What Every Tenant Should Know About Indoor Allergens* and Tenant
acknowledges receipt of such notice.
STOVE KNOB COVERS
Simultaneously with the execution of this Lease, Tenant shall complete and deliver to Owner the Annual Notice for Tenants in
Multiple Dwelling Units with gas-powered stoves annexed as a rider attached to this Lease.
AS.
NO SHORT TERM RENTAL
Under no circumstances shall Tenant put a listing for the Apartment on Airbnb or for other similar short term rental (i.e., a rental
for less than thirty (30) days), or use the Apartment for same. If Tenant does so, Owner has the right to immediately terminate this Lease.
TENANT ACKNOWLEDGES AND AGREES THAT THE FOREGOING IS A MATERIAL INDUCEMENT FOR OWNER TO ENTER
INTO THIS LEASE, AND BUT FOR SAID COVENANT, OWNER WOULD NOT HAVE EXECUTED THIS LEASE AGREEMENT.
IF
TENANT DISREGARDS THIS AGREEMENT, IN ADDITION TO THE RIGHT OF INJUNCTION, THE RIGHT TO TERMINATE THIS
LEASE ON SIX (6) DAYS' WRITTEN NOTICE TO TENANT AND ANY AND ALL REMEDIES AVAILABLE UNDER THIS LEASE AND AT
LAW OR EQUITY, TENANT WILL FORFEIT THE ENTIRE SECURITY DEPOSIT TO THE OWNER, TO COMPENSATE OWNER FOR
ANY AND ALL COSTS RELATING THERETO AS LIQUIDATED DAMAGES (AND NOT AS A PENALTY). TENANT SHALL ALSO BE
RESPONSIBLE FOR ANY AND ALL FINES AND PENALTIES IMPOSED BY ANY GOVERNMENTAL OR QUASI-GOVERNMENTAL
AGENCY OR BODY.
46.
INDEMNIFICATION
Tenant shall indemnify and save harmless Owner and Owner's agents and, at Owner's option, defend Owner and Owner's agents
against and from any and all claims against Owner and Owner's agents arising wholly or in part from any act, omission or negligence of
Tenant or the Tenant Parties. This indemnity and hold harmless agreement shall include indemnity from and against any and all liability,
fines, suits, demands, costs, damages and expenses of any kind or nature (including without limitation attorney's and other professional
fees and disbursements) incurred in or in connection with any such claims (including any settlement thereof) or proceeding br ought
thereon, and the defense thereof
47.
NOISE
Tenant shall not create any unreasonable noise levels which shall interfere with the quiet enjoyment of the other tenants of the
Building or the neighbors of the Building. Tenant agrees to promptly notify Owner in writing of all noise complaints or summons which
Tenant receives in writing, and to submit a proposal reasonably satisfactory to Owner as to how to handle same and assure that such
complaints shall not recur. TENANT ACKNOWLEDGES AND AGREES THAT THE FOREGOING IS A MATERIAL INDUCEMENT FOR OWNER
TO ENTER INTO THIS LEASE, AND BUT FOR SAID COVENANT, OWNER WOULD NOT HAVE EXECUTED THIS LEASE AGREEMENT. IF
TENANT DISREGARDS THIS AGREEMENT, IN ADDITION TO THE RIGHT OF INJUNCTION AND ANY AND ALL REMEDIES AVAILABLE
UNDER THIS LEASE AND AT LAW OR EQUITY,
TENANT WILL FORFEIT THE ENTIRE SECURITY DEPOSIT TO THE OWNER, TO
COMPENSATE OWNER FOR ANY AND ALL COSTS RELATING THERETO AS LIQUIDATED DAMAGES (AND NOT AS A PENALTY)
48.
WAIVER OF LIABILITY

Anything contained in this Lease to the contrary notwithstanding, Tenant agrees that Tenant shall look solely to the estate and
property of Owner in the Apartment or to any proceeds obtained by Owner as a result of a sale by Owner of the Apartment, for the
collection of any judgment (or other judicial process) requiring the payment of money by Owner in the event of any default or breach by
Owner with respect to any of the terms and provisions of this Lease to be observed and/or performed by Owner, subject, however, to the
prior rights of any lessor under a superior lease or holder of a superior mortgage. No other assets of Owner or any partner, officer, director
or principal of Owner, shall be subject to levy, execution or other judicial process for the satisfaction of Tenant's claim hereunder.
49.
OWNER'S APPROVAL
If Tenant shall request Owner's approval or consent and Owner shall fail or refuse to give such approval or consent, Tenant shall
not be entitled to any damages for any withholding or delay of such approval or consent by Owner, it being intended that Tenant's sole
remedy shall be an action for injunction without bond or specific performance (the rights to money damages or other remedies being
hereby specifically waived. Furthermore, such remedy shall be available only in those cases where Owner shall have expressly agreed
in writing not to unreasonably withhold its consent or approval (as applicable). or where as a matter of law, Owner may not unreasonably
withhold its consent or approval. In such event, provided Tenant is successful therein, Owner shall be responsible to pay Tenant's actual
costs and expenses incurred therein, including reasonable attorneys fees.
50.
BANKRUPTCY; INSOLVENCY
If () Tenant files a voluntary petition in bankruptcy or insolvency or are the subject of an involuntary bankruptcy proceeding, (il)
Tenant assigns property for the benefit of creditors, or (li) a non-bankruptcy trustee or receiver of Tenant's or Tenant's property is
Additional Rent and any damages, losses and expenses due Owner without offset.
51.
CONTROLLING LAW
Tenant acknowledges that by negotiating and entering into this Lease, Tenant has transacted business within the State of New
York. Any action, proceeding or claim arising out of this Lease or breach thereof, shall be litigated within the State of New York and the
parties consent to the personal jurisdiction of the courts (including the New York City Housing Court) within the State of New York and
consent that any process may be served either personally, by facsimile or by certified or registered mail, return receipt requested, to
Tenant at Tenant's address as set forth in this Lease, or in any manner provided by New York Law
Tenant shall not be entitled, directly or indirectly, to diplomatic or sovereign immunity and shall be subject to, and Tenant shall
agree to consent to, the service of process in, and the jurisdiction of, the courts of, New York State.
52.
OWNER'S CONTROL
The Lease shall not end or be modified nor will Tenant's obligations be ended or modified if for any cause not fully within Owner's
reasonable control, Owner is delayed or unable to (a) fulfill any of Owner's promises or agreements, or (b) supply any required service or
(c) make any required repairs to the Apartment
53.
COUNTERPARTS
This Lease may be executed in any number of identical counterparts and by scanned or facsimile signature, and each counterpart
hereof shall be deemed to be an original instrument, but all counterparts hereof taken together shall constitute but a single instrument
54
BINDING EFFECT
It is expressly understood and agreed that this Lease shall not constitute an offer or create any rights in Tenant's favor, and shall
in no way obligate or be binding upon Owner, and this Lease shall have no force or effect until this Lease is duly executed by Tenant and
Owner and a fully executed copy of this Lease is delivered to both Tenant and Owner.
55.
SMOKING
THERE IS NO SMOKING PERMITTED INSIDE THE APARTMENT (OR ON THE BALCONY OR TERRACE, IF ANY) UNDER
ANY CIRCUMSTANCES. IF TENANT DISREGARDS THIS AGREEMENT, TENANT WILL FORFEIT ONE-THIRD (1/3) OF THE
SECURITY DEPOSIT TO THE OWNER, TO COMPENSATE OWNER FOR ANY AND ALL COSTS RELATING THERETO AS
LIQUIDATED DAMAGES (AND NOT AS A PENALTY). TENANT ACKNOWLEDGES AND AGREES THAT THE FOREGOING IS A
MATERIAL INDUCEMENT FOR OWNER TO ENTER INTO THIS LEASE, AND BUT FOR SAID COVENANT, OWNER WOULD NOT
HAVE EXECUTED THIS LEASE AGREEMENT.
TENANT AND OWNER SHALL SIGN AND COMPLETE THE BUILDING'S SMOKING POLICY ANNEXED AS RIDER
ATTACHED TO THIS LEASE
56.
GARBAGE, REFUSE AND RECYCLING
Tenant shall comply with the rules and regulations of the Building in all respects, including, but not limited to, those regarding
garbage and recycling laws. Tenant shall not place any large articles outside of the Apartment except in compliance with the rules and
regulations of the Building in all respects. Tenant agrees to promptly pay Owner for any violations for violation of Tenant's obligations
pursuant to this Article 56.
57.
TOILETS/PLUMBING FIXTURES
The toilets and plumbing fixtures shall only be used for the purposes for which they were designed or built for. No feminine hygiene
or similar products such as paper towels may be discarded in the toilets or plumbing fixtures.
58.
EMERGENCIES
Tenant will provide Owner with list of persons to contact in the event of an emergency. Emergencies include, but are not limited
to: health and safety of Tenant or guests, water damage or fire, or unauthorized persons attempting entry into the Apartment without
Owner's knowledge.
59.
BICYCLES [DELETE IF INAPPLICABLE
60.
All bicycles are expressly forbidden in the Apartment
ALARM SYSTEM (DELETE IF INAPPLICABLE)
Fenant hereby ackner
medges and agrees tat the
must be turned on each and every
codes to Tenant to the Alarm System pr
"Alam-System") which
shat not change the Alarm
is a material inducement for
Notwithstanding the presence of the Alarm
fesponsible for any less er lost er stelen e
we executed tAIs Lease
is that Owner wilt not be-
61.
THIRD PARTY BENEFICIARY
This Lease is an agreement solely for the benefit of Owner and Tenant (and their permitted successors and/or assigns). No
person, party or entity other than Owner and Tenant shall have any rights hereunder or be entitled to rely upon the terms, covenants and
provisions contained herein. The provisions of this Article 61 shall survive the termination hereof.

62.
MOVING IN, VACATING APARTMENT AND TERMINATION
Should Owner become concerned with the inadequate care and/or supervision of Tenant's moving company's crew, Tenant
shall instruct moving personnel to comply with Owner's reasonable request for added protection throughout the Apartment. All moving
personnel must be fully insured and reasonable proof of such insurance must be supplied to Owner before moving will be permitted
on or in the Apartment.
B. In the course of Tenant's moving in, out or having items delivered to the Apartment, should there be any damage to the
halls, doors or any other part of the Apartment or the Building, Tenant shall be responsible to pay for the repair of such damage.
C. Upon the expiration of this Lease, Tenant shall return the Apartment in broom clean condition. Additional cleaning charges
incurred by Owner due to Tenant's breach of this Article 62 shall be borne by Tenant and shall be deemed Additional Rent.
63.
OWNER UNABLE TO PERFORM
Notwithstanding anything to the contrary contained in this Lease, any prevention, delay or stoppage due to strikes, lockouts, labor
disputes, acts of God, inability to obtain services, labor, or materials or reasonable substitutes therefore, governmental actions, civil
commotion, fire or other casualty, and other causes beyond the reasonable control of the party obligated to perform,
except with respect
to the obligations imposed with regard to the payment of Rent and Additional Rent to be paid by Tenant pursuant to this Lease (any of
the foregoing "Force Majeure") shall excuse the performance of such party for a period equal to any such prevention, delay or stoppage
64.
ILLEGALITY.
If a term in this Lease is illegal, invalid or unenforceable, the rest of this Lease remains in full force.
SIGNATURES CONTINUED ON NEXT PAGE

Exhibit A
MEMORANDUM CONFIRMING TERM
[DELETE IF INAPPLICABLE
THIS MEMORANDUM ("Memorandum") is made as of 04/05/2023 between ST MARKS ASSETS, ("Owner") and RAID AHMED, MICHAEL
ZIEGLER ("Tenant"), pursuant to that certain Lease Agreement between Owner and Tenant dated as of April 15, 2023 the ("Lease") for the
Apartment located at 34 ST MARKS PLACE, NEW YORK, NY 10003 (the "Apartment"), and more particularly desribed in the Lease. All initial-
capitalized terms used in this Memorandum have the meanings ascribed to them in the Lease.
Owner and Tenant hereby confirm that:
(a)
(b)
(C)
The Lease Commencement Date of the Lease Term is April
15 2023
The expiration date of the Lease Term is June.
30
2024
; and
The date Rent commences under the Lease is April
15.2023
2)
Tenant hereby confirms that:
(a)
(b)
(c)
All commitments, arrangements or understandings made to induce Tenant to enter into the Lease have been satisfied;
The condition of the Apartment complies with Owner's obligations under the Lease; and
Tenant has accepted and is in full and complete possession of the Apartment.
3)
This Memorandum shall be binding upon and inure to the benefit of the parties and their permitted successors and assigns.
IN WITNESS WHEREOF, the parties have executed this Memorandum as of the date first set forth above.
OWNER:
By:
Name: ST MARKS ASSETS
TENANT:
By:
Name: RAID AHMED
By:
Name: MICHAEL ZIEGLER
By.
Name:
By.
Name:

Exhibit B
STANDARD FORM OF APARTMENT
Lease
The Real Estate Board of New York, Inc.
Copyright 2019. All rights Reserved. Reproduction in whole or in part prohibited.
ATTACHED OWNER'S RULES AND REGULATIONS
WHICH ARE A PART OF THE LEASE AS PROVIDED BY ARTICLE 10
Public Access Ways
(a) Tenants shall not block or leave anything in or on fire escapes, the sidewalks, entrances, driveways, elevators, stairways,
or halls of the Building. Public access ways shall be used only for entering and leaving the Apartment and the Building. Only those
elevators and passageways designated by Owner can be used for deliveries.
(b) Baby carriages, bicycles or other property of Tenants shall not be allowed to stand in the halls, passageways, public areas or
common areas of the Building.
Bathroom and Plumbing Fixtures
2.
The bathrooms, toilets and wash closets and plumbing fixtures shall only be used for the purposes for which they were
designed or built; sweepings, rubbish bags, acids or other substances shall not be placed in them.
Refuse
3.
Carpets, rugs or other articles shall not be hung or shaken out of any window of the Apartment or Building. Tenants shall not
sweep or throw or permit to be swept or thrown any dirt, garbage or other substances out of the windows or into any of the halls,
elevators or elevator shafts of the Building. Tenants shall not place any articles outside of the Apartments or outside of the Building
except in safe containers and only at places designated by Owner.
Elevators
4.
All non-automatic passenger and service elevators shall be operated only by employees of Owner and must not in any event
be interfered with by Tenants. The service elevators, if any, shall be used by servants, messengers and trades people for entering and
leaving, and the passenger elevators, if any, shall not be used by them for any purpose
Laundry
5.
Laundry and drying apparatus, if any, shall be used by Tenants in the manner and at the times that the superintendent or
other representative of Owner may direct. Tenants shall not dry or air clothes on the roof.
Keys and Locks
6.
Owner may retain a pass key to the apartment. Tenants may install on the entrance of the Apartment an additional lock of
not more than three inches in circumference. Tenants may also install a lock on any window but only in the manner provided by law.
Immediately upon making any installation of either type, Tenants shall notify Owner or Owner's agent and shall give Owner or Owner's
agent a duplicate key. If changes are made to the locks or mechanism installed by Tenants, Tenants must deliver keys to Owner. At the
end of this Lease, Tenants must return to Owner all keys either furnished or otherwise obtained. If Tenants lose or fail to return any keys
which were furnished to them, Tenants shall pay to Owner the cost of replacing them.
Noise
Tenants, their families, guests, employees, or visitors shall not make or permit any disturbing noises in the Apartment or
Building or permit anything to be done that will interfere with the rights, comforts or convenience of other tenants. Also, Tenants shall not
play a musical instrument or operate or allow to be operated a CD player, radio or television set so as to disturb or annoy any other
occupant of the Building.
No Projections
8.
An aerial may not be erected on the roof or outside wall of the Building without the written consent of Owner, in Owner's sole
discretion. Also, awnings or other projections shall not be attached to the outside walls of the Building or to any balcony or terrace.
No Pets
9.
Dogs or animals of any kind shall not be kept or harbored in the Apartment, unless in each instance it be expressly permitted in
writing by Owner. This consent, if given, can be taken back by Owner at any time for good cause on reasonably given notice. Unless
carried or on a leash, pets shall not be permitted on any passenger elevator or in any public portion of the building. Also, pets are not
permitted on any grass or garden plot under any condition. THE STRICT ADHERENCE TO THE PROVISIONS OF THIS RULE BY EACH
TENANT IS A MATERIAL REQUIREMENT OF EACH LEASE. TENANT'S FAILURE TO OBEY THIS RULE SHALL BE CONSIDERED A
MATERIAL BREACH BY TENANT UNDER THE LEASE AND OWNER MAY ELECT TO END THE LEASE BASED UPON THIS
VIOLATION.
Moving
10.
Tenants can use the elevator to move furniture and possessions only on designated days and hours. Owner shall not be
liable for any costs, expenses or damages incurred by Tenants in moving because of delays caused by the unavailability of the elevator.
Floors
11.
Apartment floors shall be covered with rugs or carpeting of at least 80% of the floor area of each room excepting only
kitchens, pantries, bathrooms and hallways. The tacking strip for wall-to-wall carpeting will be glued, not nailed to the floor.
Window Guards
12.
IT IS A VIOLATION OF LAW TO REFUSE, INTERFERE WITH INSTALLATION, OR REMOVE WINDOW GUARDS WHERE
REQUIRED. (SEE ATTACHED WINDOW GUARD RIDER)
Odors
13.
Tenants shall not permit objectionable odors to emanate from the Apartment or the Building.
Smoke and Carbon Monoxide Detectors
14.
Tenants shall not remove batteries from smoke or carbon monoxide detectors or in any other way disarm them.

State of New York 
Division of Housing and Community Renewal 
Office of Rent Administration WebSite:www.nysdhcr.gov 
Pursuant to the NYC Housing Maintenance Code, an owner/managing agent of residential rental property shall furnish to each tenant signing a vacancy lease a notice that sets forth the property’s bedbug infestation history. 

. 

 

Name of tenant(s): Raiid Ahmed Subject Premises: Apt. #: Date of vacancy lease: 
Michael Ziegler 

 

[ ] Other: 
Signature of Tenant(s): 
Signature of Owner/Managing Agent: 
. 
BEDBUG INFESTATION HISTORY 
(Only boxes checked apply) 
[ ] There is no history of any bedbug infestation within the past year in the building or in any apartment. 
[ ] During the past year the building had a bedbug infestation history that has been the subject of eradication measures. The location of the infestation was on the 

floor(s). 
[ ] During the past year the building had a bedbug infestation history on the 

floor(s) and it has not been the subject of eradication measures. 
[ ] During the past year the apartment had a bedbug infestation history and eradication measures were employed. 
[ ] During the past year the apartment had a bedbug infestation history and eradication measures were not employed. 

DBB-N (9/10) 
NOTICE TO TENANT DISCLOSURE OF BEDBUG INFESTATION HISTORY 
Cynthia Graffeo 
Dated: 
Dated: 

 

 

 
Disclosure of Information on Lead-Based Paint and/or Lead-Based Paint Hazards 
Lead Warning Statement 
Housing built before 1978 may contain lead-based paint. Lead from paint, paint chips, and dust can pose health hazards if not managed properly. Lead exposure is especially harmful to young children and pregnant women. Before renting pre-1978 housing, lessors must disclose the presence of known lead-based paint and/or lead-based paint hazards in the dwelling. Lessees must also receive a federally approved pamphlet on lead poisoning prevention. 
Lessor’s Disclosure 
(a) Presence of lead-based paint and/or lead-based paint hazards (check (i) or (ii) below): 
(i) ____ Known lead-based paint and/or lead-based paint hazards are present in the housing (explain). 
(ii) ___ Lessor has no knowledge of lead-based paint and/or lead-based paint hazards in the housing. 
(b) Records and reports available to the lessor (check (i) or (ii) below): 
(i) ______ Lessor has provided the lessee with all available records and reports pertaining to lead-based paint and/or lead-based paint hazards in the housing (list documents below). 
(ii) ___ Lessor has no reports or records pertaining to lead-based paint and/or lead-based paint hazards in the housing. 
Lessee’s Acknowledgment (initial) (c) Lessee has received copies of all information listed above. (d) Lessee has received the pamphlet Protect Your Family from Lead in Your Home. 
Agent’s Acknowledgment (initial) (e) 

Agent has informed the lessor of the lessor’s obligations under 42 U.S.C. 4852(d) and 
is aware of his/her responsibility to ensure compliance. 
Certification of Accuracy 
The following parties have reviewed the information above and certify, to the best of their knowledge, that 

 

 

 

 

 

the information they have provided is true and 
accurate. 
Lessor 

 

Date Lessee 

 

Date Agent 

 

Date 
Cynthia Graffeo 
Lessor Lessee Agent 
Date Date Date 

 
LEASE/COMMENCEMENT OF OCCUPANCY NOTICE FOR PREVENTION OF LEAD BASED PAINT HAZARDS- INQUIRY REGARDING CHILD 
You are required by law to inform the owner if a child under six years of age resides or will reside in the dwelling unit (apartment) for which you are signing this lease/commencing occupancy. If such a child resides or will reside in the unit, the owner of the building is required to perform an annual visual inspection of the unit to determine the presence of lead-based paint hazards. It is important that you return this form to the owner or managing agent of your building to protect the health of your child. If you do not respond to this notice, the owner is required to attempt to inspect your apartment to determine if a child under seven years of age resides there. 

 

If a child under six years of age does not reside in the unit now, but does come to live in it at any time during the year, you must inform the owner in writing immediately. If a child under six years of age resides in the unit, you should also inform the owner immediately at the address below if you notice any peeling paint or deteriorated subsurface in the unit during the year. 
Please complete this form and return one copy to the owner or his or her agent or representative when you sign the lease/commencement occupancy of the unit. Keep one copy of this form for your records. You should also receive a copy of a pamphlet developed by the New York City Department of Health and Mental Hygiene explaining about lead based paint hazards when you sign your lease/commence occupancy. 
CHECK ONE: A child under six years of age resides in the unit. A child under six years of age does not reside in the unit. 
____________________________________________________________________ (Occupant signature) 
Print occupant’s name, address and apartment number: 
RAIID AHMED, MICHAEL ZIEGLER 34 ST MARKS PLACE Unit 3 NEW YORK, NY 10003 
(NOT APPLICABLE TO RENEWAL LEASE) Certification by owner: I certify that I have complied with the provisions of 27-2056.6 of Article 14 of the Housing Maintenance Code and the rules promulgated thereunder relating to duties to be performed in vacant units, and that I have provided a copy of the New York City Department of Health and Mental Hygiene pamphlet concerning lead based paint hazards to the occupant. 
______________________________________________________________________ (Owner signature) 

 

 

 

 

 

 

 

 

Return this form to: 
ST MARKS ASSETS 250 WEST 57TH STREET SUITE 720 NEW YORK, NY 10107 
OCCUPANT: KEEP ONE COPY FOR YOUR RECORDS OWNER COPY/OCCUPANT COPY 
RIDER: Attached to and made a part of the lease that commenced 04/15/2023, and is scheduled to expire on 06/30/2024, between: 

LANDLORD: TENANT: PREMISES: 
ST MARKS ASSETS RAIID AHMED, MICHAEL ZIEGLER 34 ST MARKS PLACE Unit 3 NEW YORK, NY 10003 

	0.	Joint and Several Liability: If Tenant is composed of more than one signatory to this Lease, each signatory will be jointly and severally liable with each other signatory for payment and performance according to this Lease.  
	0.	Late Payment / Dishonored Check Fees: Rent is due the 1st day of each month. Tenant agrees to pay a late payment fee of fifty ($50.00) dollars on all rents not received by the Landlord by the tenth (10th) of each calendar month. Landlord need not give Notice to charge the late fee. If Tenant pays rent by check and said check is dishonored by the bank on which check is drawn, Tenant will be responsible to pay Landlord dishonored check fees, in addition to the fee for late payment. These fees are added rent.  
	0.	Rent Payments: Tenant acknowledges that all rent payments are payable to either Landlord or Landlord’s agent, A.J. Clarke Real Estate Corp. and must be sent to Landlord’s lockbox facility, A. J. Clarke Real Estate Corp., P. O. Box 328, Dept. 500, Emerson, NJ 07630 or paid online through Landlord’s lockbox company. Lockbox facility is subject to change at Landlord’s or Landlord’s agent at any time. If sending payment by check, Tenant must write their ACCOUNT NUMBER ON THE RENT CHECK to ensure proper application of funds to Tenant’s account. Landlord will only accept checks in the name of the Tenant.  
	0.	Garbage and Refuse: Garbage and recyclable items must be brought to the basement or other areas designated by Landlord in such a manner that Landlord may direct. Tenants shall not place any articles of refuse outside the apartment or outside the building except in safe containers and only at places designated by Landlord and in a manner that is in accordance with local, state and federal law. For example, when disposing of a mattress, mattress must be wrapped in the proper encasement and put curbside during proper days and hours for sanitation pick-up. Tenant shall be liable to Landlord for any violations issued to Landlord as a result of Tenant’s failure to properly dispose of refuse and garbage, properly recycle or other violation of law.  
	0.	Smoke and Carbon Monoxide Alarms: Tenant acknowledges that the Premises being rented has smoke and carbon monoxide alarm(s) in proper working order. Tenant shall not remove the smoke and carbon monoxide detectors and shall replace battery when it becomes necessary.  
	0.	Furniture / Appliance Restrictions: Tenant shall not install any water bed, washing machine, dishwasher or electrical equipment which shall overtax and/or burden the existing floor load, plumbing, and/or electrical wiring in the building. A violation of such restriction shall be deemed a violation of a substantial obligation of this lease. Tenant acknowledges that Landlord is neither responsible for an air conditioner unit left in the apartment nor for any kind of service required for an air conditioner unit. In the event that there are blinds or window coverings in the apartment, Tenant acknowledges that it is not the responsibility of the Landlord to maintain.  
	0.	Air Conditioner(s): Any air conditioner(s) installed by Tenant may not exceed the capacity of the existing electrical wiring in the Premises. All window air conditioners must be self-supporting and properly mounted in accordance with local, state and federal laws and regulations and must not rely on window sashes for support. Tenant is not permitted to drill holes or screw fasteners into the window frames or sashes to support window air conditioners or for any other purpose.  
	0.	Quiet Enjoyment: Tenant must be considerate of the right to quiet enjoyment for all other tenants in the building. Stereos, TVs, etc. must be played at a volume that will not disturb neighbors. Carpets and/or rugs covering 80% of Tenant’s apartment floor area will be required if bare floors cause a noise issue to the tenant(s) living below the apartment.  
	0.	Door Locks: Landlord is only responsible for the maintenance and upkeep of the main (bottom) lock on the front door of Tenant’s apartment. Landlord must have a complete set of the apartment keys, which will be used only for purposes of inspection of any building system, repair work, emergency, or to show the apartment. Except for an emergency, Tenant will always receive reasonable notification prior to access.  
	0.	Fireplace: If there is a fireplace in the apartment, Tenant agrees that it is for decorative purposes only and cannot be used.  
	0.	Miscellaneous: Tenant covenants and agrees not to put excessive nails, wallpaper, or other foreign material onto the demised premises or to paint the walls any color but the color of the walls of the apartment as given to Tenant at the time of taking possession of the Premises. Any bicycles, carriages or any other wheeled vehicles must be kept within the apartment itself.  
	0.	Use of Premises: It is agreed that the Premises will only be used as a residence and not as corporate housing or place of business. Tenant acknowledges and agrees to not sublet, rent or barter the Premises for use by anyone other than Tenant without the express written authorization by Landlord. Tenant further acknowledges and agrees to not enlist the services of companies including but not limited to Craig’s List and Airbnb, Inc. to sublet, rent or barter the Premises without the express written consent of Landlord. Tenant shall not utilize the Premises or any part of the Premises for any commercial use and shall not, under any circumstances, rent or utilize the Premises or any part of the Premises for short-term occupancy and/or transient occupancy. Tenant shall not advertise the rental of the Premises nor any part of the Premises on any rental websites such as www.airbnb.com, craigslist.org or other similar web sites or advertising enterprises. A violation of this provision shall be deemed a substantial breach of the Tenant’s obligations under the Lease and Tenant’s tenancy. In addition, Tenant shall indemnify and hold harmless Landlord and its principals, agents and employees for any and all fines, penalties, costs (including but not limited to attorneys’ fees) imposed upon Landlord or incurred by Landlord by reason of Tenant’s violation of this provision.  
	0.	Sprinkler Disclosure: Please take notice pursuant to Article 7, Section 231-A of the New York State Real Property Law that the Premises Tenant is leasing does not contain a maintained and operative sprinkler system.  
	0.	Utility Services and Charges: Tenant expressly acknowledges and agrees to establish and be responsible for any and all utility services including but not limited to electric and gas usage upon commencement of the Lease. Tenant agrees to immediately contact the appropriate utility company that services the area of the Premises (usually Consolidated Edison) and establish an account for electric and gas usage for the Premises. If Tenant fails to establish an utility account, and the utility company in turn charges the Landlord for utility services consumed in the Premises, then Tenant understands and agrees that Landlord will back charge Tenant in the amount of any and all said utility costs plus an administrative fee of one hundred ($100.00) dollars per month until Tenant establishes a utility account for the Premises and Landlord is no longer being billed for said utility services.  
	0.	Security Deposit: Tenant acknowledges and agrees that the security deposit is not meant to be applied as rent payment for Tenant’s final month of rent, or any other month of rent. Said sum will be returned to Tenant in accordance with the terms of this Lease, provided all terms and conditions of this Lease have been met and Tenant has physically vacated the demised Premises, surrendered vacant possession of the Premises, is current on all monies due and returned all building, apartment and mailbox keys to Landlord or Landlord’s agent. Landlord, however, does have the right to apply security deposit against any arrears of Tenant.  
	0.	Sublet: Tenant acknowledges and agrees that the apartment cannot be sublet or assigned without the express written consent of Landlord.  
	0.	Renters Insurance: Landlord requires that Tenant purchase renters insurance to insure Tenant’s personal property against any damage or loss that may occur. Tenant acknowledges Landlord’s requirement of renters insurance and agrees to purchase renters insurance. Tenant agrees to name Landlord and Landlord’s agent as an additional insured party in Tenant’s renters insurance policy. In the event that Tenant fails to obtain necessary insurance, Tenant agrees to indemnify the Landlord and managing agent and hold them harmless against any and all claims for damage to Tenant’s personal property. Tenant must supply a copy of the certificate of insurance to the Landlord’s agent within thirty (30) days of occupancy.  
	0.	Lease Application: Tenant’s lease application is incorporated by reference and made a part of this Lease. Tenant represents, warrants and affirms that the information on Tenant’s lease application is true and accurate. Tenant understands and agrees that Landlord relies on the accuracy of the information provided on the lease application submitted by a prospective tenant in order to determine whether or not to offer this Lease to the applicant. It is a substantial, material and non-curable obligation of this Lease that all information provided on Tenant’s lease application is true and accurate. Tenant understands and agrees that it is a substantial, non-curable violation and a material, non- curable default of Tenant’s Lease and tenancy if any of the information submitted by Tenant on Tenant’s lease application is not true and accurate. The submission of false and/or inaccurate information by Tenant on Tenant’s lease application is deemed to be a non-curable default of this Lease and entitles Landlord to terminate Tenant’s Lease and tenancy on ten (10) days written notice, without providing Tenant with an opportunity to cure said default.  
	0.	Lease Expiration: Tenant understands the terms and conditions of this Lease and acknowledges that Landlord is under no obligation to offer any extension or renewal to Tenant. Should Landlord offer Tenant a renewal, Tenant agrees to notify Landlord at least sixty (60) days prior to the lease expiration by written notice if Tenant will be renewing or vacating the Premises. Tenant’s failure to notify Landlord by written notice at lease sixty (60) days in advance of the lease expiration date of Tenant’s intention to renew or vacate the Premises may result in penalties up to the equivalent of one month’s rent. If Tenant does not renew the lease, Landlord has the right to commence showing the apartment for rental a minimum of sixty (60) days prior to the lease expiration date. Tenant also agrees that Landlord may conduct a vacature inspection any time from thirty (30) days prior to the lease expiration or the vacate date upon twenty-four (24) hours verbal notice to Tenant. Tenant’s failure to provide proper notice or access as described herein may result in monetary penalties up to the equivalent of one month’s rent. Any articles remaining in the Premises after Tenant vacates will be considered abandoned by Tenant and at the election of Landlord, shall either be left in the Premises or removed and disposed of by Landlord; the costs associated with same may be deducted from the security deposit. Tenant shall be responsible for Landlord’s expenses and/or damages resulting from removal and/or disposal of abandoned property or restoration of the apartment Premises to correct any damage caused by removal of Tenant’s installation.  
	0.	Lease Execution: This Lease may be executed via facsimile or e-mail and in any number of counterparts, each of which will be deemed an original, but which together shall constitute one and the same instrument.  
A.J. Clarke Real Estate Corp., Agent 
By: ____________________________ ST MARKS ASSETS, Landlord 
By: ______________________________ RAIID AHMED, Tenant 
By: ______________________________ MICHAEL ZIEGLER, Tenant 
By: ______________________________ , Tenant 
By: ______________________________ , Tenant 
Rev. 2019-0812: AJC - FM 
THE REAL ESTATE BOARD OF NEW YORK, INC. SPRINKLER DISCLOSURE LEASE RIDER 
Pursuant to the New York State Real Property Law, Article 7, Section 231-a, effective December 3, 2014 all residential leases must contain a conspicuous notice as to the existence or non-existence of a Sprinkler System in the Leased Premises. 
Name of tenant(s): Lease Premises Address: Apartment Number: Date of Lease: CHECK ONE: 
__RAIID AHMED, MICHAEL ZIEGLER, _ _34 ST MARKS PLACE_NEW YORK, NY 10003_ _3 _ (the "Leased Premises") __ 

 

 

	0.	[ X ] There is NO Maintained and Operative Sprinkler System in the Leased Premises.  
	0.	[ ] There is a Maintained and Operative Sprinkler System in the Leased Premises  
A. The last date on which the Sprinkler System was maintained and inspected was on ______________. 
A "Sprinkler System" is a system of piping and appurtenances designed and installed in accordance with generally accepted standards so that heat from a fire will automatically cause water to be discharged over the fire area to extinguish it or prevent its further spread (Executive Law of New York, Article 6-C, Section 155-a(5)). _________________________________________________________________________________ 
Acknowledgment & Signatures: 
I, the Tenant, have read the disclosure set forth above. I understand that this notice, as to the existence or non-existence of a Sprinkler System is being provided to me to help me make an informed decision about the Leased Premises in accordance with New York State Real Property Law Article 7, Section 231 -a. 

Tenant: 
Owner: 
Name: _RAIID AHMED_ Signature: ________________________________ Date: _________________ Name: _MICHAEL ZIEGLER_ Signature: ________________________________ Date: _________________ Name: __ Signature: ________________________________ Date: _________________ Name: __ Signature: ________________________________ Date: _________________ Name: _ST MARKS ASSETS_ Signature: ________________________________ Date: _________________ 

 

 

 

RAIID AHMED, MICHAEL ZIEGLER 
34 ST MARKS PLACE NEW YORK, NY 10003 
3 
ST MARKS ASSETS 
250 WEST 57TH STREET SUITE 720 NEW YORK, NY 10107 
General Smoking Policy for Residential Buildings 
Building/Property Address: 34 ST MARKS PLACE Unit 3 NEW YORK, NY 10003 
There is no safe amount of exposure to secondhand smoke. Adults exposed to secondhand smoke have higher risks of stroke, heart disease and lung cancer. Children exposed to secondhand smoke have higher risks of asthma attacks, respiratory illnesses, middle ear disease and sudden infant death syndrome (SIDS). For these reasons, and to help people make informed decisions on where to live, New York City requires residential building owners (referred to in this policy as the “Owner/Manager,” which includes the owner of record, seller, manager, landlord, any agent thereof or governing body) in buildings with three or more residential units to create a policy on smoking and share it with all tenants. The building policy on smoking applies to any person on the property, including guests. 

Definitions a. Smoking: inhaling, exhaling, burning or carrying any lighted or heated cigar, cigarette, 

little cigar, pipe, water pipe or hookah, herbal cigarette, non-tobacco smoking product (e.g., marijuana or non-tobacco shisha), or any similar form of lighted object or device designed for people to use to inhale smoke 
b. Electronic Cigarette (e-cigarette): a battery-operated device that heats a liquid, gel, herb or other substance and produces vapor for people to inhale 
Smoke-Free Air Act 
New York City law prohibits smoking and using e-cigarettes of any kind in indoor common areas, including but not limited to, lobbies, hallways, stairwells, mailrooms, fitness areas, storage areas, garages and laundry rooms in any building with three or more residential units. NYC Admin. Code, § 17-505. 

Policy on Smoking 
Smoking is not allowed in the locations checked below (check all boxes that apply). Even if no boxes are checked, the Smoke-Free Air Act bans smoking tobacco or non-tobacco products and using e-cigarettes in indoor common areas. 

□ Inside of residential units* □ Outside of areas that are part of residential units, including balconies, patios and porches 
□ Outdoor common areas, including play areas, rooftops, pool areas, parking areas, 
and shared balconies, courtyards, patios, porches or yards □ Outdoors within 15 feet of entrances, exits, windows, and air intake units on property 
grounds □ Other areas/exceptions: 
______________________________________________________________________
______________________________________________________________________
______________________________________________________________________
____________________________________________________________________
General Smoking Policy for Residential Buildings Continued 
*Rent-stabilized and rent-controlled units may be exempt from a policy restricting smoking inside residential units unless the existing tenant consents to the policy in writing. 
Complaints should be made in writing and should be as specific as possible, including the date, approximate time, location where smoke was observed, building address, description of incident and apparent source of smoke. 
Complaint Procedure 
Complaints about smoke drifting into a residential unit or common area should be made promptly to the Owner/Manager listed here ST MARKS ASSETS. 

Acknowledgment and Signatures: 
I have read the policy on smoking described above, and I understand the policy applies to the property. I agree to comply with the policy described above. 
For rental units, I understand that violating the smoking policy may be a violation of my lease. For condominiums, cooperatives or other owned units, I understand that violations of the policy on smoking may be addressed according to the building’s governing rules. 
Owner/Manager’s printed name: ST MARKS ASSETS 
Owner/Manager’s signature: ________________________ 
RAIID AHMED Tenant’s printed name: ____________________________ 
Tenant’s signature: ______________________________ 
MICHAEL ZIEGLER Tenant’s printed name: ____________________________ 
Tenant’s signature: ______________________________ Tenant’s printed name: ____________________________ Tenant’s signature: ______________________________ Tenant’s printed name: ____________________________ Tenant’s signature: ______________________________ 
Date: ___________ Date: ___________ Date: ___________ Date: ___________ Date: ___________ Date: ___________ Date: ___________ Date: ___________ Date: ___________ 

 
LEASE/COMMENCEMENT OF OCCUPANCY NOTICE FOR INDOOR ALLERGEN HAZARDS 
1. The owner of this building is required, under New York City Administrative Code section 27- 2017.1 et seq., to make an annual inspection for indoor allergen hazards (such as mold, mice, rats, and cockroaches) in your apartment and the common areas of the building. The owner must also inspect if you inform him or her that there is a condition in your apartment that is likely to cause an indoor allergen hazard, or you request an inspection, or the Department has issued 
a violation requiring correction of an indoor allergen hazard for your apartment. If there is an indoor allergen hazard in your apartment, the owner is required to fix it, using the safe work practices that are provided in the law. The owner must also provide new tenants with a pamphlet containing information about indoor allergen hazards. 
2. The owner of this building is also required, prior to your occupancy as a new tenant, to fix all visible mold and pest infestations in the apartment, as well as any underlying defects, like leaks, using the safe work practices provided in the law. If the owner provides carpeting or furniture, he or she must thoroughly clean and vacuum it prior to occupancy. This notice must be signed by the owner or his or her representative, and state that he or she has complied with these requirements. 
I, ST MARKS ASSETS (owner or representative name in print), certify that I have complied with the requirements of the New York City Administrative Code section 27- 2017.5 by removing all visible mold and pest infestations and any underlying defects, and where applicable, cleaning and vacuuming any carpeting and furniture that I have provided to the tenant. I have performed the required work using the safe work practices provided in the law. 
Signed: Scott Clarke 
Print Name: ST MARKS ASSETS Date: 4/5/2023 

 

 
What Every Tenant Should Know About Indoor Allergens and the Asthma- Free Housing Act (Local Law 55) 
Allergens are things in the environment that make indoor air quality worse. They can cause asthma attacks or make asthma symptoms worse. Common indoor allergens, or triggers, include cockroaches and mice; mold and mildew; and chemicals with strong smells, like some cleaning products. Environmental and structural conditions, like leaks and cracks in walls often found in poorly maintained housing, lead to higher levels of allergens. New York City law requires that landlords take steps to keep their tenants’ homes free of pests and mold. This includes safely fixing the conditions that cause these problems. Tenants also play a role in preventing indoor allergens. 
Tenants should: 
• Keep homes clean and dry • Place food in sealed containers, keep counters and sinks clean, and get rid of clutter such as newspapers and paper bags • Use garbage cans with tight-fitting lids • Take garbage and recycling out every day, and tie up garbage bags before putting them in compactor chutes • Avoid using pesticides and chemicals with strong smells (e.g., cleaning products, air fresheners, etc.) • Tell landlords right away if there are pests, water leaks, or holes or cracks in the walls and floors • Let building staff into homes to make any needed repairs • Call 311 if landlords do not fix the problem or if repair work is being done unsafely 
If you are a tenant and you or your child has asthma, and there are pests or mold in your home, your doctor can request a free home environmental inspection for you through the New York City Health Department’s Online Registry. Talk to your doctor or call 311 to learn more. 
For more information about building owner and landlord responsibilities and safely fixing indoor allergen hazards, see the reverse side of this handout. 
For more information about safely controlling asthma, visit nyc.gov/health/asthma. 
ةيبرعلا | Español | 繁體中文| 简体中文 | Русский |한국어| Kreyòl ayisyen nyc.gov/health “healthy neighborhoods” 

 

 

 

 
What Landlords Must Do to Keep Homes Free of Pests and Mold 
New York City law requires that landlords of buildings with three or more apartments - or buildings of any size where a tenant has asthma - take steps to keep tenant homes free of pests and mold. This includes safely fixing the conditions that cause these problems. 
Landlords must: 
· Inspect every apartment and the building’s common areas for cockroach and rodent infestations, mold and the conditions that lead to these hazards, at least once a year and more often if necessary. Landlords must also respond to tenant complaints or requests for an inspection. 
· Use integrated pest management (IPM) practices to safely control pests and fix building-related issues that lead to pest problems. 
ü Remove pest nests and thoroughly clean pest waste and other debris using a HEPA vacuum. Make sure to limit the spread of dust when cleaning. 
ü Repair and seal any holes, gaps or cracks in walls, ceilings, floors, molding, base boards, around pipes and conduits, and around and within cabinets. 
	•			ü Attach door sweeps to all doors that lead to hallways, basements or outside.  
	•			ü Remove all water sources for pests by repairing drains, faucets and other plumbing materials that collect water or  
leak. ü Use pesticides sparingly. If pesticides must be used to correct a violation, they must be applied by a New York 
State Department of Environmental Conservation-licensed pest professional. 
· Remove indoor mold and safely fix the problems that cause mold. ü Remove any standing water, and fix leaks or moisture conditions. ü Move or cover furniture, and seal off doorways, ventilation ducts and other openings securely with plastic 
sheeting. ü Gently spray the moldy area with soap or detergent and water before cleaning to limit the spread of dust. ü Clean the work area with wet mops or HEPA vacuums before work starts, at the end of each day and after all repair 
work is completed. ü Dry the cleaned area completely.  Throw away all cleaning-related waste in heavy-duty plastic bags and seal 
securely. ü To clean 10 or more square feet of mold in a building with 10 or more apartments, landlords must hire a New York 
State Department of Labor-licensed mold assessor and remediator. Per New York City Administrative Code section 24-154 and New York State Labor Law Article 32, assessors and remediators must submit paperwork to the New York City Department of Environmental Protection. 
	•			· Make sure vacant apartments are thoroughly cleaned and free of pests and mold before a new tenant moves in.  
	•			· Provide a copy of this fact sheet and a notice with each tenant’s lease that clearly states the landlord’s and tenant’s  
responsibilities to keep the building free of indoor allergens. 
For more information about building owner and landlord responsibilities and safely fixing indoor allergen hazards, visit nyc.gov/hpd and search for indoor allergen hazards 
ةيبرعلا | Español | 繁體中文| 简体中文 | Русский |한국어| Kreyòl ayisyen nyc.gov/health “healthy neighborhoods” 
"""
summary = ""

substrings = split_string(long_string)

for i, substring in enumerate(substrings):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful research assistant."},
            {"role": "user", "content": f"Summarize this: {substring}"},
        ],
    )

    page_summary = response["choices"][0]["message"]["content"]
    summary += page_summary + "\n"

    with open("Summary.txt", "w+") as file:
        file.write(summary)

with open("Summary.txt", "r") as file:
    print(file.read())







